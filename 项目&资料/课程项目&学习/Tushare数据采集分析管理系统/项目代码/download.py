# download.py
import tushare as ts
import sqlite3
import pandas as pd
import os

# 你的Tushare token
TUSHARE_TOKEN = '68c780abc209b67280b95bf6f125fc23c3efe05299c34e5b4e6e8da6'

# 数据库文件名
DATABASE = 'stock_data.db'

# 表名常量
TOTAL_TABLE = 'daily_data'
BJ_TABLE = 'daily_data_bj'
SH_TABLE = 'daily_data_sh'

# 建表 SQL 模板
TABLE_SCHEMA = '''
CREATE TABLE IF NOT EXISTS {table_name} (
    ts_code TEXT,
    trade_date TEXT,
    open_price REAL,
    high_price REAL,
    low_price REAL,
    close_price REAL,
    pre_close_price REAL,
    change REAL,
    pct_chg REAL,
    vol REAL,
    amount REAL,
    PRIMARY KEY (ts_code, trade_date)
)
'''

def fetch_and_store_daily_data(start_date, end_date):
    # 1. 设置 token
    ts.set_token(TUSHARE_TOKEN)
    pro = ts.pro_api()

    # 2. 获取每日股票交易数据
    if start_date and end_date:
        data = pro.daily(start_date=start_date, end_date=end_date)
    else:
        data = pro.daily()  # 返回 DataFrame
    if data is None or data.empty:
        print("No daily data fetched.")
        return

    # 3. 重命名列以匹配数据库字段名
    data = data.rename(columns={
        'open': 'open_price',
        'high': 'high_price',
        'low': 'low_price',
        'close': 'close_price',
        'pre_close': 'pre_close_price',
        'change': 'change',
        'pct_chg': 'pct_chg',
        'vol': 'vol',
        'amount': 'amount'
    })

    # 4. 按 ts_code 后缀分割 DataFrame (Tushare ts_code 后缀通常是大写 .SH 或 .SZ)
    bj_data = data[data['ts_code'].str.upper().str.endswith('.BJ', na=False)]
    sh_data = data[data['ts_code'].str.upper().str.endswith('.SH', na=False)]

    # 5. 建立数据库连接
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # 6. 创建三张表：总表、BJ 表、SH 表
    cursor.execute(TABLE_SCHEMA.format(table_name=TOTAL_TABLE))
    cursor.execute(TABLE_SCHEMA.format(table_name=BJ_TABLE))
    cursor.execute(TABLE_SCHEMA.format(table_name=SH_TABLE))

    # 7. 写入数据到各表（推荐用 append 或 replace 单条插入）
    # 全量表
    data.to_sql(TOTAL_TABLE, conn, if_exists='append', index=False)
    # BJ 分表
    if not bj_data.empty:
        bj_data.to_sql(BJ_TABLE, conn, if_exists='replace', index=False)
    # SH 分表
    if not sh_data.empty:
        sh_data.to_sql(SH_TABLE, conn, if_exists='replace', index=False)

    # 8. 提交并关闭连接
    conn.commit()
    conn.close()

    print(f"Successfully stored {len(data)} total records, {len(bj_data)} BJ records and {len(sh_data)} SH records.")

# 从环境变量中读取采集时间范围
START_DATE = os.getenv('START_DATE', None)
END_DATE = os.getenv('END_DATE', None)

if __name__ == '__main__':
    # 使用环境变量中的时间范围调用采集函数
    fetch_and_store_daily_data(start_date=START_DATE, end_date=END_DATE)
