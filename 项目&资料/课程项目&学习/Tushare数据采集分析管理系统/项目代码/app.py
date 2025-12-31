from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.stock import bp as stock_bp
from routes.auth import bp as auth_bp
# 确保你已经创建了 routes/forum.py 文件，否则会报 ModuleNotFoundError
try:
    from routes.forum import bp as forum_bp  # 新增
except ModuleNotFoundError:
    forum_bp = None
import os
from config import DATABASE
import sqlite3


def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
    CORS(app)
    app.secret_key = 'your_secret_key'

    # 注册蓝图
    app.register_blueprint(stock_bp)
    app.register_blueprint(auth_bp)
    if forum_bp:
        app.register_blueprint(forum_bp)  # 新增

    @app.route('/static/<path:filename>')
    def static_files(filename):
        static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))
        return send_from_directory(static_dir, filename)

    return app


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    def static_files(filename):
        static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))
        return send_from_directory(static_dir, filename)

    @app.route('/')
    def index():
        return render_template('index.html')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
