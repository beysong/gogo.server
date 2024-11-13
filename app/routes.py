from flask import Blueprint, render_template, request, Response, jsonify
from datetime import datetime

from . import db
from .models import Product, ErrorLog, User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/create_product', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        # 如果不存在 则新建，否则什么也不做

        proItem = Product.query.filter_by(productUrl=data['productUrl']).first()
        if proItem:
            return Response('OK 已存在', 200)

        print(data['proName'])
        product = Product(name=data['proName'],
            shop_id=data['shop_id'],
            main_image=data['proImg'],
            image_list=data['skuImgs'],
            proSkuName=data['skuProName'],
            proPrice=float(data['proPrice']),
            productUrl=data['productUrl'],
            proAttrNames=data['proAttrNames'],
            proAttrValues=data['proAttrValues'],
            descImgs=data['descImgs'],
            breadCrumb=data['breadCrumb'],
            proParams=data['proParams'],
            proPmodel=data['proPmodel'],
            proCategoryIds=data['proCategoryIds'],
            proPacking=data['packing'],
            proBrand=data['proBrand'],
            )
        # product = Product(name='test')
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        data = request.json
        error = ErrorLog(content=jsonify(data), error_text=str(e))
        db.session.add(error)
        db.session.commit()
        return Response(str(e), 500)
        

    return Response('OK')

@main_bp.route('/update_product', methods=['POST'])
def update_product():

    data = request.get_json()
    print(data)
    new_pro = {
        "descImgs": data['descImgs']
    }
    err, result = Product.update(data['id'], new_pro)
    if err:
        return Response(err, 500)
    return Response('OK')
