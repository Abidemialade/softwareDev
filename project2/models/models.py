from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    category = db.Column(db.String(50), nullable=False)  # "Men" or "Women"
    size = db.Column(db.String(10), nullable=False)       # e.g., "S", "M", "L"



class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100))  # For guest carts
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)
    product = db.relationship('Product', backref='cart_items')



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)  
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    total_amount = db.Column(db.Float)
    shipping_name = db.Column(db.String(100))
    shipping_address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    zip_code = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

