from flask import Blueprint, render_template, request, Response, jsonify
from datetime import datetime

from . import db
from .models.user import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/create_product', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
    except Exception as e:
        return Response(str(e), 500)
        

    return Response('OK')
