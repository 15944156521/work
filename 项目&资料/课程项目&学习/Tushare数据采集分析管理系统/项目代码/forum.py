from flask import Blueprint, request, jsonify
from config import DATABASE
import sqlite3
import datetime

bp = Blueprint('forum', __name__, url_prefix='/api/forum')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@bp.route('/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT id, title, content, author, created_at FROM forum_posts ORDER BY created_at DESC').fetchall()
    conn.close()
    return jsonify([dict(row) for row in posts])

@bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author = data.get('author', '匿名')
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not title or not content:
        return jsonify({'error': '标题和内容不能为空'}), 400
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO forum_posts (title, content, author, created_at) VALUES (?, ?, ?, ?)',
        (title, content, author, created_at)
    )
    conn.commit()
    conn.close()
    return jsonify({'msg': '发帖成功'})

@bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT id, title, content, author, created_at FROM forum_posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post:
        return jsonify(dict(post))
    else:
        return jsonify({'error': '未找到该帖子'}), 404

@bp.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM forum_posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return jsonify({'msg': '删除成功'})
