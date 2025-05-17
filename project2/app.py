from flask import Flask, render_template, request, redirect, url_for, flash, session
from config import Config
from models.models import db, Product, User, Order
from sqlalchemy import text, asc, desc
from sqlalchemy.orm import load_only
from werkzeug.security import generate_password_hash, check_password_hash

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
    if 'user_id' not in session:
        flash("Please log in to proceed to checkout.")
        return redirect(url_for('login'))

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

    if request.method == 'POST':
        new_order = Order(
            user_id=session['user_id'],
            total_amount=total,
            shipping_name=request.form['shipping_name'],
            shipping_address=request.form['shipping_address'],
            city=request.form['city'],
            zip_code=request.form['zip_code']
        )
        db.session.add(new_order)
        db.session.commit()

        session['cart'] = []  # Clear cart
        flash("Order submitted successfully.")
        return redirect(url_for('order_confirmation', order_id=new_order.id))

    return render_template('checkout.html', cart_items=cart_items, total=total)

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

    # Only seed if product table is empty
    if not Product.query.first():
        sizes = ["S", "M", "L", "XL"]
        men_products = [
            "men_hoodie1.jpg", "men_hoodie2.jpg", "men_hoodie3.jpg",
            "men_jacket1.jpg",
            "men_shirt1.jpg", "men_shirt2.jpg", "men_shirt3.jpg", "men_shirt4.jpg"
        ]
        women_products = [
            "women_hoodie1.jpg", "women_hoodie2.jpg",
            "women_jacket1.jpg", "women_jacket2.jpg", "women_jacket3.jpg", "women_jacket4.jpg",
            "women_shirt1.jpg", "women_shirt2.jpg"
        ]
        sample_products = []

        for filename in men_products:
            name = filename.replace(".jpg", "").replace("_", " ").title()
            for size in sizes:
                sample_products.append(Product(
                    name=name,
                    price=round(49.99 + hash(filename + size) % 100, 2),
                    stock=10,
                    category="Men",
                    size=size,
                    image_url=f"/static/images/{filename}"
                ))

        for filename in women_products:
            name = filename.replace(".jpg", "").replace("_", " ").title()
            for size in sizes:
                sample_products.append(Product(
                    name=name,
                    price=round(49.99 + hash(filename + size) % 100, 2),
                    stock=10,
                    category="Women",
                    size=size,
                    image_url=f"/static/images/{filename}"
                ))

        db.session.bulk_save_objects(sample_products)
        db.session.commit()
        print("✅ Seeded 64 products.")






# Run app
if __name__ == '__main__':
    app.run(debug=True)