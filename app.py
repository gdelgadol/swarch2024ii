from flask import Flask, render_template, request, redirect, url_for
from models.products import db
from controllers.product_controller import product_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.17.0.2:3306/swarch2024ii_db'
db.init_app(app)
app.register_blueprint(product_blueprint)

products = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/products', methods=['POST'])
def add_product():
    name = request.form['name']
    description = request.form['description']
    products.append({'name': name, 'description': description})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
