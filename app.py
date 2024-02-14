# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Baby Diapers", "price": 10.99},
    {"id": 2, "name": "Baby Wipes", "price": 5.99},
    # Add more products as needed
]

# Shopping cart
cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    total_price = sum(item['price'] for item in cart)
    return render_template('checkout.html', cart=cart, total_price=total_price)

@app.route('/complete_order', methods=['POST'])
def complete_order():
    # In a real application, you would process the order, update the database, etc.
    cart.clear()
    return render_template('order_complete.html')

if __name__ == '__main__':
    app.run(debug=True)
