# backend/db.py

import sqlite3
from typing import List, Dict, Any

import pandas as pd

from config import DATABASE  # 确保这里是从 config.py 导入

def connect_db():
    """
    连接到SQLite数据库，返回连接对象
    """
    return sqlite3.connect(DATABASE)

def get_table_names():
    """
    查询数据库中所有表名
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    return [table[0] for table in tables]



def connect_db() -> sqlite3.Connection:
    """
    连接到 SQLite 数据库，返回连接对象
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# backend/db.py
import sqlite3
from typing import List, Dict, Any

from config import DATABASE


def connect_db() -> sqlite3.Connection:
    """
    连接到 SQLite 数据库，返回连接对象
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def _batch_upsert(table: str, records: List[Dict[str, Any]]):
    """
    通用批量删除旧纪录并插入新纪录逻辑
    """
    conn = connect_db()
    cursor = conn.cursor()
    # 删除旧数据
    delete_sql = f"DELETE FROM {table} WHERE ts_code=? AND trade_date=?;"
    insert_sql = f'''
    INSERT INTO {table}
      (ts_code, trade_date,
       open_price, high_price, low_price, close_price,
       pre_close_price, change, pct_chg, vol, amount)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
    delete_params = [(rec['ts_code'], rec['trade_date']) for rec in records]
    cursor.executemany(delete_sql, delete_params)

    # 批量插入新数据
    insert_params = [(
        rec['ts_code'], rec['trade_date'],
        rec.get('open_price'), rec.get('high_price'), rec.get('low_price'), rec.get('close_price'),
        rec.get('pre_close_price'), rec.get('change'), rec.get('pct_chg'),
        rec.get('vol'), rec.get('amount')
    ) for rec in records]
    cursor.executemany(insert_sql, insert_params)

    conn.commit()
    conn.close()


def insert_daily_data(records: List[Dict[str, Any]]):
    """
    将记录批量更新到 daily_data 表
    """
    _batch_upsert('daily_data', records)


def insert_daily_data_sh(records: List[Dict[str, Any]]):
    """
    将记录批量更新到 daily_data_sh 表
    """
    _batch_upsert('daily_data_sh', records)


def insert_daily_data_bj(records: List[Dict[str, Any]]):
    """
    将记录批量更新到 daily_data_bj 表
    """
    _batch_upsert('daily_data_bj', records)


def get_some_data(limit=5):
    """
    查询daily_data表的部分数据，默认返回前5条
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM daily_data LIMIT {limit};")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def create_basic_tables():
    """
    创建基础数据表，包括用户表、股票信息表等
    """
    conn = connect_db()
    cursor = conn.cursor()
    # 创建用户表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        );
    ''')
    # 创建股票信息表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_info (
            ts_code TEXT UNIQUE,
            name TEXT,
            market TEXT
        );
    ''')
    # 创建基金信息表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fund_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fund_code TEXT UNIQUE,
            name TEXT
        );
    ''')
    # 创建用户收藏股票表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_fav_stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            ts_code TEXT,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(ts_code) REFERENCES stock_info(ts_code)
        );
    ''')
    # 创建用户收藏基金表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_fav_fund (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            fund_code TEXT,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(fund_code) REFERENCES fund_info(fund_code)
        );
    ''')
    # 创建股票每日数据表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts_code TEXT,
            trade_date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            FOREIGN KEY(ts_code) REFERENCES stock_info(ts_code)
        );
    ''')
    # 创建系统日志表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sys_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            user_id INTEGER,
            timestamp TEXT,
            FOREIGN KEY(user_id) REFERENCES user(id)
        );
    ''')
    conn.commit()
    conn.close()

def auto_collect_stock_info(limit=400):
    """
    自动采集股票基础信息并写入数据库
    :param limit: 限制采集的股票数量（默认400条）
    """
    import tushare as ts
    from config import TUSHARE_TOKEN
    ts.set_token(TUSHARE_TOKEN)
    pro = ts.pro_api()
    df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name,market')
    if df.empty:
        print("自动采集失败：未获取到股票数据")
        return
    df = df.head(limit)  # 限制采集数量
    conn = connect_db()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            'INSERT OR REPLACE INTO stock_info (ts_code, name, market) VALUES (?, ?, ?)',
            (row['ts_code'], row['name'], row['market'])
        )
    conn.commit()
    conn.close()
    print(f"自动采集成功：共采集 {len(df)} 条股票数据")

def print_all_users():
    """
    打印user表中所有用户的信息
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, password, is_admin FROM user;")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def print_all_stocks():
    """
    打印stock_info表中所有股票的信息
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT ts_code, name, market FROM stock_info;")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def print_daily_data(limit=5):
    """
    打印daily_data表中的部分数据
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM daily_data LIMIT ?", (limit,))
    for row in cursor.fetchall():
        print(row)
    conn.close()

def print_daily_data_columns():
    """
    打印 daily_data 表的字段名
    """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(daily_data);")
    for row in cursor.fetchall():
        print(row)
    conn.close()

if __name__ == "__main__":
    from config import DATABASE
    print("数据库文件路径为：", DATABASE)
    print("数据库中的表有：", get_table_names())
    create_basic_tables()
    print("已确保 stock_info 表存在。")
    auto_collect_stock_info(limit=400)  # 限制采集前 400 条股票数据
    print_all_users()
    print_all_stocks()  # 打印所有股票信息，辅助调试
    print_daily_data(10)  # 打印 daily_data 表的前 10 条数据
    print_daily_data_columns()  # 打印 daily_data 表的字段名
    # clear_user_table()  # 清空 user 表，执行一次后请注释掉，避免下次误删
    print_all_stocks()  # 打印所有股票信息，辅助调试
    print_daily_data(10)  # 打印 daily_data 表的前 10 条数据
    print_daily_data_columns()  # 打印 daily_data 表的字段名
    # clear_user_table()  # 清空 user 表，执行一次后请注释掉，避免下次误删
    # clear_user_table()  # 清空 user 表，执行一次后请注释掉，避免下次误删
    print("user 表已清空。")


def get_all_data():
    """
    读取 daily_data 表的所有数据并返回 pandas.DataFrame
    """
    conn = connect_db()
    try:
        # 将整个 daily_data 表读入 DataFrame
        df = pd.read_sql_query("SELECT * FROM daily_data", conn)
        return df
    finally:
        conn.close()