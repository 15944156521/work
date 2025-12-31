from flask import Blueprint, request, jsonify, session
import sqlite3
import hashlib
from config import DATABASE  # 添加这一行

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if not username or not password or not email:
        return jsonify({'error': '用户名、密码和邮箱必填'}), 400

    # 加密密码
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    try:
        conn.execute('INSERT INTO user (username, password, email) VALUES (?, ?, ?)', 
                     (username, hashed_password, email))
        conn.commit()
        return jsonify({'msg': '注册成功'})
    except sqlite3.IntegrityError:
        return jsonify({'error': '用户名或邮箱已存在'}), 409
    finally:
        conn.close()

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    user = conn.execute('SELECT * FROM user WHERE username=?', (username,)).fetchone()
    conn.close()
    # 兼容明文和加密密码
    if user and (user['password'] == hashed_password or user['password'] == password):
        session['user_id'] = user['id']
        session['username'] = user['username']
        session['is_admin'] = user['is_admin']
        log_action(user['id'], '登录')
        return jsonify({'msg': '登录成功', 'is_admin': user['is_admin']})
    return jsonify({'error': '用户名或密码错误'}), 401

@bp.route('/profile', methods=['GET'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登录'}), 401
    conn = get_db()
    user = conn.execute('SELECT id, username FROM user WHERE id=?', (user_id,)).fetchone()
    conn.close()
    return jsonify(dict(user)) if user else ('', 404)

@bp.route('/change_password', methods=['POST'])
def change_password():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登录'}), 401

    data = request.json
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()

    conn = get_db()
    user = conn.execute('SELECT * FROM user WHERE id=?', (user_id,)).fetchone()
    if not user or user['password'] != hashed_old_password:
        conn.close()
        return jsonify({'error': '原密码错误'}), 400

    conn.execute('UPDATE user SET password=? WHERE id=?', (hashed_new_password, user_id))
    conn.commit()
    conn.close()
    log_action(user_id, '修改密码')
    return jsonify({'msg': '密码修改成功'})

@bp.route('/update_permission', methods=['POST'])
def update_permission():
    user_id = session.get('user_id')
    is_admin = session.get('is_admin', 0)
    if not user_id or not is_admin:
        return jsonify({'error': '无权限'}), 403

    data = request.json
    target_user_id = data.get('user_id')
    new_permission = data.get('is_admin')

    if new_permission not in [0, 1]:
        return jsonify({'error': '权限值无效'}), 400

    conn = get_db()
    cursor = conn.cursor()

    # 获取当前权限值
    current_permission = cursor.execute('SELECT is_admin FROM user WHERE id=?', (target_user_id,)).fetchone()
    if not current_permission:
        conn.close()
        return jsonify({'error': '目标用户不存在'}), 404

    # 更新权限值
    cursor.execute('UPDATE user SET is_admin=? WHERE id=?', (new_permission, target_user_id))
    conn.commit()

    # 记录日志
    log_action(user_id, f"更新用户权限: 用户ID {target_user_id}, 原权限 {current_permission['is_admin']}, 新权限 {new_permission}")

    conn.close()
    return jsonify({'msg': '权限更新成功'})

@bp.route('/sys_log', methods=['GET'])
def sys_log():
    user_id = session.get('user_id')
    is_admin = session.get('is_admin', 0)
    if not user_id or not is_admin:
        return jsonify({'error': '无权限'}), 403
    conn = get_db()
    logs = conn.execute(
        "SELECT sys_log.id, sys_log.user_id, user.username, sys_log.action, sys_log.timestamp "
        "FROM sys_log LEFT JOIN user ON sys_log.user_id = user.id "
        "ORDER BY sys_log.timestamp DESC LIMIT 100"
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in logs])

# 在用户操作时记录日志的辅助函数
def log_action(user_id, action):
    conn = get_db()
    conn.execute('INSERT INTO sys_log (user_id, action, timestamp) VALUES (?, ?, CURRENT_TIMESTAMP)',
                 (user_id, action))
    conn.commit()
    conn.close()
