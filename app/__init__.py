from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decimal import Decimal
import json

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_filename=None):
    app = Flask(__name__)
    # app.json_encoder = CustomJSONEncoder

    if config_filename:
        app.config.from_pyfile(config_filename)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app


# 自定义 JSON 编码器
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # 将 Decimal 转换为 float
            return float(obj)  # 或者使用 str(obj) 将其转换为字符串
        return super().default(obj)