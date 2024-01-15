from app import db
# импортируется объект db из модуля app

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), nullable=False)
    driver = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(10), nullable=False, unique=True)
    on_duty = db.Column(db.Boolean, default=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    car = db.relationship('Car', backref=db.backref('orders', lazy=True))
    passenger = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    sms_code = db.Column(db.String(4), nullable=False)

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)