from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import Config
from models.models import db, Product, User, Order
from sqlalchemy import text, asc, desc
from sqlalchemy.orm import load_only
from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy
db.init_app(app)

# Homepage
@app.route('/')
def index():
    seen_men = set()
    men_products = []
    for p in Product.query.filter_by(category="Men").all():
        if p.name not in seen_men:
            men_products.append(p)
            seen_men.add(p.name)

    seen_women = set()
    women_products = []
    for p in Product.query.filter_by(category="Women").all():
        if p.name not in seen_women:
            women_products.append(p)
            seen_women.add(p.name)

    return render_template('index.html', men_products=men_products, women_products=women_products)



# Category pages 
@app.route('/category/<category>')
def category(category):
    normalized_category = category.capitalize()

    size = request.args.get('size')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    sort = request.args.get('sort')

    query = Product.query.filter_by(category=normalized_category)

    if size:
        query = query.filter_by(size=size)
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    # Sorting
    if sort == 'price_asc':
        query = query.order_by(asc(Product.price))
    elif sort == 'price_desc':
        query = query.order_by(desc(Product.price))
    elif sort == 'name_asc':
        query = query.order_by(asc(Product.name))
    elif sort == 'name_desc':
        query = query.order_by(desc(Product.name))


    seen_names = set()
    products = []
    for p in query.all():
        name_clean = p.name.replace('Men ', '').replace('Women ', '')
        if name_clean not in seen_names:
            p.name = name_clean
            products.append(p)
            seen_names.add(name_clean)
    return render_template('category.html', category=normalized_category, products=products)


# Product detail page 
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)


# Shopping cart
@app.route('/cart')
def cart():
    cart_data = session.get('cart', [])
    cart_items = []
    total = 0

    for item in cart_data:
        product = Product.query.get(item['product_id'])
        if product:
            cart_items.append({
                'id': product.id,
                'name': product.name,
                'image_url': product.image_url,
                'price': product.price,
                'size': item['size']
            })
            total += product.price

    return render_template('cart.html', cart_items=cart_items, total=total)


@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    size = request.form.get('size')
    cart = session.get('cart', [])
    cart.append({'product_id': product_id, 'size': size})
    session['cart'] = cart  
    flash("Item added to cart!")
    return redirect(url_for('product_detail', product_id=product_id))

@app.route('/update-cart', methods=['POST'])
def update_cart():
    cart = session.get('cart', [])
    for item in cart:
        item_id = item['product_id']
        quantity = request.form.get(f'quantity_{item_id}')
        if quantity:
            item['quantity'] = int(quantity)
    session['cart'] = cart


@app.route('/remove-from-cart/<int:product_id>/<size>', methods=['POST'])
def remove_from_cart(product_id, size):
    cart = session.get('cart', [])
    cart = [item for item in cart if not (item['product_id'] == product_id and item['size'] == size)]
    session['cart'] = cart
    return redirect(url_for('cart'))



# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered.")
            return redirect(url_for('register'))

        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password_hash=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created. Please log in.")
        return redirect(url_for('login'))

    return render_template('register.html')


# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash("Logged in successfully.")
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password.")

    return render_template('login.html')


# User logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))


#checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        cart_data = session.get('cart', [])
        cart_items = []
        total = 0
        for item in cart_data:
            product = Product.query.get(item['product_id'])
            if product:
                cart_items.append({
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'size': item['size']
                })
                total += product.price
        return render_template('checkout.html', cart_items=cart_items, total=total)

    # Handle POST (form submission)
    if 'user_id' not in session:
        flash("You must be logged in to checkout.", "warning")
        return redirect(url_for('login'))

    user_id = session['user_id']
    cart = session.get('cart', [])
    if not cart:
        flash("Your cart is empty.", "error")
        return redirect(url_for('cart'))

    shipping_name = request.form.get('shipping_name')
    shipping_address = request.form.get('shipping_address')
    city = request.form.get('city')
    zip_code = request.form.get('zip_code')
    total = sum(Product.query.get(item['product_id']).price for item in cart if Product.query.get(item['product_id']))

    items_json = json.dumps(cart)

    new_order = Order(
        user_id=user_id,
        total_amount=total,
        shipping_name=shipping_name,
        shipping_address=shipping_address,
        city=city,
        zip_code=zip_code,
        items=items_json
    )
    db.session.add(new_order)
    db.session.commit()
    session.pop('cart', None)
    flash("Order submitted successfully!")
    return redirect(url_for('order_confirmation', order_id=new_order.id))


# Order confirmation
@app.route('/order-confirmation/<int:order_id>')
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_confirmation.html', order=order)


@app.route('/all-products')
def show_all_products():
    products = Product.query.all()
    return '<br>'.join(
        [f"{p.id}. {p.name} — {p.category} — {p.size} — ${p.price} — {p.image_url}" for p in products]
    )


with app.app_context():
    #db.drop_all() 
    db.create_all()

    # Only seed if product table is empty. This adds all products to the database.
    if not Product.query.first():
        sizes = ["S", "M", "L", "XL"]

        men_products = [
            "men/hoodie1.jpg", "men/hoodie2.jpg", "men/hoodie3.jpg",
            "men/jacket1.jpg",
            "men/shirt1.jpg", "men/shirt2.jpg", "men/shirt3.jpg", "men/shirt4.jpg"
        ]

        women_products = [
            "women/hoodie1.jpg", "women/hoodie2.jpg",
            "women/jacket1.jpg", "women/jacket2.jpg", "women/jacket3.jpg",
            "women/shirt1.jpg", "women/shirt2.jpg",
            "women/sweatshirt1.jpg"
        ]

        product_name_map = {
            # Men
            "hoodie1.jpg": "Essential Rhude Hoodie",
            "hoodie2.jpg": "Zip-Up Hoodie",
            "hoodie3.jpg": "Oversized Pullover Hoodie",
            "shirt1.jpg": "Relaxed Silk Shirt",
            "shirt2.jpg": "Classic Fit T-Shirt",
            "shirt3.jpg": "Casual T-Shirt",
            "shirt4.jpg": "Linen Button-Down Shirt",
            "jacket1.jpg": "Utility Bomber Jacket",

            # Women
            "hoodie1.jpg": "Boxy Fit Hoodie",
            "hoodie2.jpg": "Cropped Hoodie",
            "shirt1.jpg": "Oversized Shirt",
            "shirt2.jpg": "Jersey Blouse",
            "sweatshirt1.jpg": "Sky Blue Sweatshirt",
            "jacket1.jpg": "Red Leather Jacket",
            "jacket2.jpg": "Black Longsleeve Jacket",
            "jacket3.jpg": "Brown Leather Jacket"
        }

        sample_products = []

        for path in men_products:
            key = path.split("/")[-1]  # hoodie1.jpg
            clean_name = product_name_map.get(key, key.replace(".jpg", "").replace("_", " ").title())
            for size in sizes:
                sample_products.append(Product(
                    name=clean_name,
                    price=round(49.99 + hash(path + size) % 100, 2),
                    stock=10,
                    category="Men",
                    size=size,
                    image_url=f"/static/images/{path}"
                ))

        for path in women_products:
            key = path.split("/")[-1]
            clean_name = product_name_map.get(key, key.replace(".jpg", "").replace("_", " ").title())
            for size in sizes:
                sample_products.append(Product(
                    name=clean_name,
                    price=round(49.99 + hash(path + size) % 100, 2),
                    stock=10,
                    category="Women",
                    size=size,
                    image_url=f"/static/images/{path}"
                ))

        db.session.bulk_save_objects(sample_products)
        db.session.commit()
        print("✅ Seeded 64 products.")




# Run app
if __name__ == '__main__':
    app.run(debug=True)