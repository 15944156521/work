# backend/get_last_days_data.py
import tushare as ts
from datetime import datetime
from typing import List, Dict, Any
import sys

import db


def get_last_5_days_stock_data(ts_code: str, token: str) -> List[Dict[str, Any]]:
    """
    获取指定股票代码最近5个交易日的数据，并返回为字典列表，字段与数据库表对应
    """
    ts.set_token(token)
    pro = ts.pro_api()

    end_date = datetime.today().strftime('%Y%m%d')
    try:
        df = pro.daily(
            ts_code=ts_code,
            end_date=end_date,
            limit=5,
            sort='desc'
        )
    except Exception as e:
        print(f"Tushare 接口调用失败: {e}", file=sys.stderr)
        return []

    if df is None or df.empty:
        print(f"未找到股票 {ts_code} 的历史数据", file=sys.stderr)
        return []

    # 重命名字段以匹配表结构
    df = df.rename(columns={
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

    # 确保所有必要字段存在
    expected_cols = ['trade_date', 'open_price', 'high_price', 'low_price', 'close_price',
                     'pre_close_price', 'change', 'pct_chg', 'vol', 'amount']
    missing = [col for col in expected_cols if col not in df.columns]
    if missing:
        print(f"返回数据中缺失字段: {missing}", file=sys.stderr)
        return []

    records: List[Dict[str, Any]] = df.to_dict(orient='records')
    for rec in records:
        rec['ts_code'] = ts_code
    # 打印记录，帮助调试
    print("Fetched records:")
    for rec in records:
        print(rec)
    return records


def update_and_save(ts_code: str, token: str):
    """
    获取最近5日行情并保存到通用表和对应交易所子表中，同时打印保存结果
    """
    records = get_last_5_days_stock_data(ts_code, token)
    if not records:
        print("没有可保存的记录", file=sys.stderr)
        return

    suffix = ts_code.split('.')[-1].upper()

    # 写入通用表
    try:
        db.insert_daily_data(records)
    except Exception as e:
        print(f"写入通用表失败: {e}", file=sys.stderr)

    # 写入分表
    try:
        if suffix == 'SH':
            db.insert_daily_data_sh(records)
        elif suffix == 'BJ':
            db.insert_daily_data_bj(records)
    except Exception as e:
        print(f"写入分表失败: {e}", file=sys.stderr)

    print(f"已更新并保存 {ts_code} 最近5日数据，共 {len(records)} 条。")

    # 验证写入
    from db import connect_db
    conn = connect_db()
    cursor = conn.cursor()
    # 查询通用表
    cursor.execute(
        "SELECT * FROM daily_data WHERE ts_code=? ORDER BY trade_date DESC LIMIT 5;", (ts_code,)
    )
    print("通用表最新记录:")
    for row in cursor.fetchall():
        print(dict(row))
    # 查询分表
    table = 'daily_data_sh' if suffix == 'SH' else 'daily_data_bj' if suffix == 'BJ' else None
    if table:
        cursor.execute(
            f"SELECT * FROM {table} WHERE ts_code=? ORDER BY trade_date DESC LIMIT 5;", (ts_code,)
        )
        print(f"{table} 最新记录:")
        for row in cursor.fetchall():
            print(dict(row))
    conn.close()


if __name__ == '__main__':
    from config import TUSHARE_TOKEN
    if len(sys.argv) > 1:
        TS_CODE = sys.argv[1]
    else:
        TS_CODE = '688800.SH'
    update_and_save(TS_CODE, TUSHARE_TOKEN)
