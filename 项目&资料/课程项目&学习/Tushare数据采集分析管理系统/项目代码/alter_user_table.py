import sqlite3

conn = sqlite3.connect('stock_data.db')
c = conn.cursor()

try:
    c.execute('ALTER TABLE user ADD COLUMN email TEXT;')
    print("已添加 email 字段。")
except Exception as e:
    print("添加 email 字段时出错：", e)

conn.commit()
conn.close()