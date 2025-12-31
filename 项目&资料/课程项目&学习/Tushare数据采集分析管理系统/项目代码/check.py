import sqlite3
import os

# 假设数据库文件名是 stock_data.db，和脚本同目录
db_path = os.path.join(os.path.dirname(__file__), 'stock_data.db')
print(f"Trying to open database file at: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:", tables)

    if ('daily_data',) in tables:
        cursor.execute("SELECT * FROM daily_data LIMIT 5;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    else:
        print("No table named 'daily_data' found!")

    conn.close()
except Exception as e:
    print("Error opening database:", e)
