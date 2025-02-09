from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.products_service import ProductService
product_blueprint = Blueprint('products', __name__)
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.form
    name = data.get('name')
    description = data.get('description')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    ProductService.create_product(name, description)
    return redirect(url_for('products.index'))
@product_blueprint.route('/products', methods=['GET'])
def get_products():
    products = ProductService.get_products()
    return jsonify(products)
@product_blueprint.route('/')
def index():
    return render_template('index.html')