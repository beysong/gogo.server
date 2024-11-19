from flask import Flask
from .config import config
from .extensions import db, migrate, ma, jwt, login_manager


def create_app(config_name='dev'):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config.get(config_name, 'dev'))
        
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

