# config.py
import os

# 数据库文件路径
DATABASE = os.getenv('DATABASE', os.path.join(os.path.dirname(__file__), 'stock_data.db'))

# 从环境变量中读取采集参数
TUSHARE_TOKEN = os.getenv('TUSHARE_TOKEN', '68c780abc209b67280b95bf6f125fc23c3efe05299c34e5b4e6e8da6')

# 默认采集时间范围
START_DATE = os.getenv('START_DATE', '20250101')
END_DATE = os.getenv('END_DATE', '20251231')
