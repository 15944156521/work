# backend/create_tables.py

import sqlite3
from config import DATABASE   # 确保你的 config.py 里有：DATABASE = 'stock_data.db'
from werkzeug.security import generate_password_hash

def create_user_and_admin_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # 管理员表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL
        );
    ''')

    # 用户表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            is_admin INTEGER DEFAULT 0
        );
    ''')
    # 日志表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sys_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # 插入管理员账号（如不存在）
    cursor.execute("SELECT * FROM user WHERE username=?", ('王春成',))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO user (username, password, is_admin) VALUES (?, ?, 1)", ('王春成', '123'))
    conn.commit()
    conn.close()
    print("admin 和 user 表已创建（若已存在则跳过），管理员已初始化。")

if __name__ == '__main__':
    create_user_and_admin_tables()
    create_user_and_admin_tables()
