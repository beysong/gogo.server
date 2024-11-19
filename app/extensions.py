from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_login import LoginManager

# 创建扩展实例
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()

# 配置登录视图 (未登录时自动跳转到的视图)
login_manager.login_view = 'auth.login'  # 假设有一个蓝图名为 'auth' 且登录视图名为 'login'
login_manager.login_message = "请先登录以访问此页面。"
login_manager.login_message_category = "info"
