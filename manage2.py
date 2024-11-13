
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://futurelabs:123456@127.0.0.1:3306/pyjd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float(10, 2))
    main_image = db.Column(db.String(128))
    brand = db.Column(db.String(64))
    category = db.Column(db.String(64))
    description = db.Column(db.Text)
    params = db.Column(db.Text)



@app.cli.command()  # 注册为命令，可以传入 name 参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Grey Li'
    movies = [
        {'name': 'My Neighbor Totoro', 'brand': '1988'},
        {'name': 'Dead Poets Society', 'brand': '1989'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Product(name=m['name'], brand=m['brand'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')