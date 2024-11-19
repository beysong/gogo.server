import os

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')  # 密钥（从环境变量中获取或使用默认值）
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:123456@127.0.0.1:3306/gogo')  # 数据库 URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用 Flask-SQLAlchemy 的事件系统以节省资源

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True  # 启用调试模式
    SQLALCHEMY_ECHO = True  # 显示 SQL 语句，用于调试

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True  # 启用测试模式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/gogo'  # 使用内存数据库
    WTF_CSRF_ENABLED = False  # 禁用 CSRF 保护，方便测试

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False  # 关闭调试模式
    # 生产环境下的数据库配置可以在环境变量中设置，例如 PostgreSQL 或 MySQL 的 URI

# 配置映射
config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
}
