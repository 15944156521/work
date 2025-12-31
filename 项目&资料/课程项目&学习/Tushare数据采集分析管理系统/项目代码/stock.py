from flask import Blueprint, request, jsonify, session
from config import DATABASE
import sqlite3
from datetime import datetime
import os
import matplotlib
matplotlib.use('Agg')  # 关键：使用无界面后端，防止服务器无显示环境时报错
import matplotlib.pyplot as plt
import pandas as pd
from flask import current_app, send_from_directory
import io
import base64

bp = Blueprint('stock', __name__, url_prefix='/api')

DB_PATH = './stock_data.db'  # 你的数据库路径，确保正确


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 方便通过列名访问
    return conn


def log_action(user_id, action):
    print("log_action called", user_id, action)  # 调试用
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sys_log (user_id, action) VALUES (?, ?)", (user_id, action))
    conn.commit()
    conn.close()


@bp.route('/stocks', methods=['GET'])
def get_all_stocks():
    """获取所有股票数据，支持分页"""
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 50))
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM daily_data')
    total = cursor.fetchone()[0]

    cursor.execute(
        'SELECT * FROM daily_data LIMIT ? OFFSET ?', (per_page, offset)
    )
    rows = cursor.fetchall()
    conn.close()

    # 转成字典列表
    data = [dict(row) for row in rows]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total': total,
        'stocks': data
    })


@bp.route('/stocks/<string:ts_code>', methods=['GET'])
def get_stock_by_code(ts_code):
    """根据股票代码查询所有记录"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM daily_data WHERE ts_code = ? ORDER BY trade_date DESC', (ts_code,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return jsonify({'error': 'Stock code not found'}), 404

    data = [dict(row) for row in rows]
    return jsonify(data)


@bp.route('/stocks/chart/<string:ts_code>', methods=['GET'])
def get_stock_chart_data(ts_code):
    """获取股票指定日期范围的K线图数据"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # 参数校验
    if not start_date or not end_date:
        return jsonify({'error': 'Please provide start_date and end_date in YYYYMMDD format'}), 400

    try:
        datetime.strptime(start_date, '%Y%m%d')
        datetime.strptime(end_date, '%Y%m%d')
    except ValueError:
        return jsonify({'error': 'Date format must be YYYYMMDD'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT trade_date, open, high, low, close, vol
        FROM daily_data
        WHERE ts_code = ?
          AND trade_date BETWEEN ? AND ?
        ORDER BY trade_date
    """, (ts_code, start_date, end_date))
    rows = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in rows]
    return jsonify(data)


@bp.route('/stocks/latest', methods=['GET'])
def get_latest_stocks():
    """获取最新交易日的所有股票数据"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(trade_date) FROM daily_data')
    latest_date = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM daily_data WHERE trade_date = ?', (latest_date,))
    rows = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in rows]

    return jsonify({
        'trade_date': latest_date,
        'stocks': data
    })


@bp.route('/user_fav_stocks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_fav_stocks():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登录'}), 401
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        rows = cursor.execute('SELECT * FROM user_fav_stock WHERE user_id=?', (user_id,)).fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    data = request.json
    if request.method == 'POST':
        cursor.execute('INSERT INTO user_fav_stock (user_id, ts_code, name, market) VALUES (?, ?, ?, ?)',
                       (user_id, data['ts_code'], data['name'], data['market']))
        conn.commit()
        conn.close()
        log_action(user_id, f"关注股票: {data['ts_code']} {data.get('name','')}")
        return jsonify({'msg': '关注成功'})
    if request.method == 'PUT':
        cursor.execute('UPDATE user_fav_stock SET name=?, market=? WHERE user_id=? AND ts_code=?',
                       (data['name'], data['market'], user_id, data['ts_code']))
        conn.commit()
        conn.close()
        log_action(user_id, f"更新关注股票: {data['ts_code']} {data.get('name','')}")
        return jsonify({'msg': '更新成功'})
    if request.method == 'DELETE':
        cursor.execute('DELETE FROM user_fav_stock WHERE user_id=? AND ts_code=?', (user_id, data['ts_code']))
        conn.commit()
        conn.close()
        log_action(user_id, f"取消关注股票: {data['ts_code']}")
        return jsonify({'msg': '删除成功'})


@bp.route('/user_fav_funds', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_fav_funds():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登录'}), 401
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        rows = cursor.execute('SELECT * FROM user_fav_fund WHERE user_id=?', (user_id,)).fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    data = request.json
    if request.method == 'POST':
        cursor.execute('INSERT INTO user_fav_fund (user_id, fund_code, name) VALUES (?, ?, ?)',
                       (user_id, data['fund_code'], data['name']))
        conn.commit()
        conn.close()
        log_action(user_id, f"关注基金: {data['fund_code']} {data.get('name','')}")
        return jsonify({'msg': '关注成功'})
    if request.method == 'PUT':
        cursor.execute('UPDATE user_fav_fund SET name=? WHERE user_id=? AND fund_code=?',
                       (data['name'], user_id, data['fund_code']))
        conn.commit()
        conn.close()
        log_action(user_id, f"更新关注基金: {data['fund_code']} {data.get('name','')}")
        return jsonify({'msg': '更新成功'})
    if request.method == 'DELETE':
        cursor.execute('DELETE FROM user_fav_fund WHERE user_id=? AND fund_code=?', (user_id, data['fund_code']))
        conn.commit()
        conn.close()
        log_action(user_id, f"取消关注基金: {data['fund_code']}")
        return jsonify({'msg': '删除成功'})


# 修改 /api/stock_info 和 /api/fund_info 权限控制
@bp.route('/stock_info', methods=['GET', 'POST', 'PUT', 'DELETE'])
def stock_info():
    is_admin = session.get('is_admin', 0)
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        rows = cursor.execute('SELECT * FROM stock_info').fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    if not is_admin:
        conn.close()
        return jsonify({'error': '无权限'}), 403
    data = request.json

    def validate_stock_info(data):
        if not data.get('ts_code') or not data.get('name') or not data.get('market'):
            return '缺少必要字段'
        if not isinstance(data['ts_code'], str) or not data['ts_code'].endswith(('.SZ', '.SH', '.BJ')):
            return '股票代码格式不正确'
        if not isinstance(data['name'], str) or len(data['name']) > 50:
            return '股票名称长度超出限制'
        if data['market'] not in ['主板', '创业板', '北交所']:
            return '市场类型不正确'
        return None

    validation_error = validate_stock_info(data)
    if validation_error:
        conn.close()
        return jsonify({'error': validation_error}), 400

    try:
        if request.method == 'POST':
            cursor.execute('INSERT INTO stock_info (ts_code, name, market) VALUES (?, ?, ?)',
                           (data['ts_code'], data['name'], data['market']))
            conn.commit()
            conn.close()
            return jsonify({'msg': '添加成功'})
        if request.method == 'PUT':
            cursor.execute('UPDATE stock_info SET name=?, market=? WHERE ts_code=?',
                           (data['name'], data['market'], data['ts_code']))
            conn.commit()
            conn.close()
            return jsonify({'msg': '更新成功'})
        if request.method == 'DELETE':
            cursor.execute('DELETE FROM stock_info WHERE ts_code=?', (data['ts_code'],))
            conn.commit()
            conn.close()
            return jsonify({'msg': '删除成功'})
    except sqlite3.IntegrityError as e:
        conn.rollback()
        conn.close()
        return jsonify({'error': f'数据库错误: {str(e)}'}), 400


@bp.route('/fund_info', methods=['GET', 'POST', 'PUT', 'DELETE'])
def fund_info():
    is_admin = session.get('is_admin', 0)
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        rows = cursor.execute('SELECT * FROM fund_info').fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])
    # 权限控制：只有管理员才能进行写操作
    if not is_admin:
        conn.close()
        return jsonify({'error': '无权限'}), 403
    data = request.json
    if request.method == 'POST':
        cursor.execute('INSERT INTO fund_info (fund_code, name) VALUES (?, ?)',
                       (data['fund_code'], data['name']))
        conn.commit()
        conn.close()
        return jsonify({'msg': '添加成功'})
    if request.method == 'PUT':
        cursor.execute('UPDATE fund_info SET name=? WHERE fund_code=?',
                       (data['name'], data['fund_code']))
        conn.commit()
        conn.close()
        return jsonify({'msg': '更新成功'})
    if request.method == 'DELETE':
        cursor.execute('DELETE FROM fund_info WHERE fund_code=?', (data['fund_code'],))
        conn.commit()
        conn.close()
        return jsonify({'msg': '删除成功'})


@bp.route('/daily_data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def daily_data():
    is_admin = session.get('is_admin', 0)
    user_id = session.get('user_id')
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        offset = (page - 1) * per_page
        cursor.execute('SELECT COUNT(*) FROM daily_data')
        total = cursor.fetchone()[0]
        cursor.execute('''
            SELECT 
                ts_code, 
                trade_date, 
                open_price AS open, 
                high_price AS high, 
                low_price AS low, 
                close_price AS close, 
                pre_close_price AS pre_close, 
                change, 
                pct_chg, 
                vol, 
                amount 
            FROM daily_data 
            LIMIT ? OFFSET ?
        ''', (per_page, offset))
        rows = cursor.fetchall()
        conn.close()
        data = [dict(row) for row in rows]
        return jsonify({
            'page': page,
            'per_page': per_page,
            'total': total,
            'data': data
        })

    data = request.json

    if request.method == 'POST':
        if not is_admin:
            conn.close()
            return jsonify({'error': '无权限'}), 403
        try:
            # 注意：这里必须用数据库真实字段名（open_price等），不能用open等别名
            cursor.execute('''
                INSERT INTO daily_data (ts_code, trade_date, open_price, high_price, low_price, close_price, pre_close_price, change, pct_chg, vol, amount)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['ts_code'], data['trade_date'], data['open'], data['high'], data['low'],
                data['close'], data['pre_close'], data['change'], data['pct_chg'], data['vol'], data['amount']
            ))
            conn.commit()
            # 日志
            log_action(session.get('user_id'), f"添加日线数据: {data['ts_code']} {data['trade_date']}")
            return jsonify({'msg': '添加成功'})
        except Exception as e:
            conn.rollback()
            return jsonify({'error': str(e)}), 400
        finally:
            conn.close()

    if request.method == 'PUT':
        if not is_admin:
            conn.close()
            return jsonify({'error': '无权限'}), 403
        try:
            cursor.execute('''
                UPDATE daily_data SET open_price=?, high_price=?, low_price=?, close_price=?, pre_close_price=?, change=?, pct_chg=?, vol=?, amount=?
                WHERE ts_code=? AND trade_date=?
            ''', (
                data['open'], data['high'], data['low'], data['close'], data['pre_close'],
                data['change'], data['pct_chg'], data['vol'], data['amount'],
                data['ts_code'], data['trade_date']
            ))
            conn.commit()
            return jsonify({'msg': '更新成功'})
        except Exception as e:
            conn.rollback()
            return jsonify({'error': str(e)}), 400
        finally:
            conn.close()

    if request.method == 'DELETE':
        if not is_admin:
            conn.close()
            return jsonify({'error': '无权限'}), 403
        try:
            cursor.execute('DELETE FROM daily_data WHERE ts_code=? AND trade_date=?',
                           (data['ts_code'], data['trade_date']))
            conn.commit()
            return jsonify({'msg': '删除成功'})
        except Exception as e:
            conn.rollback()
            return jsonify({'error': str(e)}), 400
        finally:
            conn.close()


@bp.route('/daily_data/fav', methods=['POST'])
def fav_daily_data():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': '未登录'}), 401
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO user_fav_stock (user_id, ts_code, name, market)
            VALUES (?, ?, ?, ?)
        ''', (user_id, data['ts_code'], data.get('name', ''), data.get('market', '')))
        conn.commit()
        return jsonify({'msg': '关注成功'})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 400
    finally:
        conn.close()


@bp.route('/collect', methods=['POST'])
def collect_data():
    is_admin = session.get('is_admin', 0)
    if not is_admin:
        return jsonify({'error': '无权限'}), 403
    params = request.json or {}
    start_date = params.get('start_date')
    end_date = params.get('end_date')
    # 调用 download.py 采集逻辑
    from download import fetch_and_store_daily_data
    try:
        fetch_and_store_daily_data(start_date, end_date)
        return jsonify({'msg': '采集成功'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/collect_stock_info', methods=['POST'])
def collect_stock_info():
    """
    管理员手动采集股票基础信息（stock_info）
    """
    from flask import session
    is_admin = session.get('is_admin', 0)
    if not is_admin:
        return jsonify({'error': '无权限'}), 403

    try:
        import tushare as ts
        from config import TUSHARE_TOKEN
        ts.set_token(TUSHARE_TOKEN)
        pro = ts.pro_api()
        df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,market')
        if df.empty:
            return jsonify({'error': '采集失败，无数据'})
        # 写入数据库
        conn = get_db_connection()
        cursor = conn.cursor()
        for _, row in df.iterrows():
            cursor.execute(
                'INSERT OR REPLACE INTO stock_info (ts_code, name, market) VALUES (?, ?, ?)',
                (row['ts_code'], row['name'], row['market'])
            )
        conn.commit()
        conn.close()
        return jsonify({'msg': f'采集成功，共{len(df)}条'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 确保 Flask 静态目录配置正确
STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

@bp.route('/visualize', methods=['POST'])
def visualize():
    """
    股票数据可视化接口
    输入: ts_code, start_date, end_date
    输出: 价格趋势图和成交量图（base64图片）
    """
    data = request.json or {}
    ts_code = data.get('ts_code')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # 输入校验
    if not ts_code or not start_date or not end_date:
        return jsonify({'error': '参数缺失'}), 400
    if not isinstance(ts_code, str) or not ts_code.endswith(('.SZ', '.SH', '.BJ')):
        return jsonify({'error': '股票代码格式不正确'}), 400
    try:
        datetime.strptime(start_date, '%Y%m%d')
        datetime.strptime(end_date, '%Y%m%d')
    except ValueError:
        return jsonify({'error': '日期格式必须为YYYYMMDD'}), 400

    conn = get_db_connection()
    df = pd.read_sql_query(
        "SELECT trade_date, open_price, close_price, vol FROM daily_data WHERE ts_code=? AND trade_date>=? AND trade_date<=? ORDER BY trade_date",
        conn, params=(ts_code, start_date, end_date)
    )
    conn.close()

    if df.empty:
        return jsonify({'error': '无数据'}), 404

    # 限制最大数据点数
    max_points = 100
    if len(df) > max_points:
        df = df.iloc[::len(df)//max_points]

    # 生成价格趋势图
    buf1 = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.plot(df['trade_date'], df['open_price'], label='开盘价', marker='o')
    plt.plot(df['trade_date'], df['close_price'], label='收盘价', marker='x')
    plt.xticks(rotation=45)
    plt.legend()
    plt.title(f"{ts_code} 价格趋势")
    plt.tight_layout()
    plt.savefig(buf1, format='png')
    plt.close()
    buf1.seek(0)
    price_chart_b64 = base64.b64encode(buf1.read()).decode('utf-8')

    # 生成成交量图
    buf2 = io.BytesIO()
    plt.figure(figsize=(10, 3))
    plt.bar(df['trade_date'], df['vol'], color='skyblue')
    plt.xticks(rotation=45)
    plt.title(f"{ts_code} 成交量")
    plt.tight_layout()
    plt.savefig(buf2, format='png')
    plt.close()
    buf2.seek(0)
    vol_chart_b64 = base64.b64encode(buf2.read()).decode('utf-8')

    return jsonify({
        'price_chart': f'data:image/png;base64,{price_chart_b64}',
        'vol_chart': f'data:image/png;base64,{vol_chart_b64}'
    })


@bp.route('/stocks_by_market', methods=['GET'])
def stocks_by_market():
    """
    按市场分类返回所有股票信息
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT ts_code, name, market FROM stock_info')
    rows = cursor.fetchall()
    conn.close()
    stocks = [dict(row) for row in rows]
    result = {}
    for stock in stocks:
        market = stock['market'] or '未知'
        if market not in result:
            result[market] = []
        result[market].append(stock)
    return jsonify(result)


@bp.route('/all_ts_codes_with_days', methods=['GET'])
def get_all_ts_codes_with_days():
    """
    获取所有有日线数据的股票代码及其数据天数
    """
    min_days = int(request.args.get('min_days', 5))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 查询每个股票代码的数据天数，只返回天数大于等于min_days的
    cursor.execute('''
        SELECT ts_code, COUNT(*) as days 
        FROM daily_data 
        GROUP BY ts_code 
        HAVING COUNT(*) >= ?
        ORDER BY COUNT(*) DESC
    ''', (min_days,))
    
    rows = cursor.fetchall()
    conn.close()
    
    # 转换为前端需要的格式
    ts_codes = [{'ts_code': row[0], 'days': row[1]} for row in rows]
    
    return jsonify({'ts_codes': ts_codes})

