from flask import Flask, render_template
# импортирует класс `Flask` из модуля `flask`
from sqlalchemy import MetaData
# импортируется класс MetaData из библиотеки SQLAlchemy - это объект, который содержит информацию о базе данных SQL
from flask_sqlalchemy import SQLAlchemy
# импортируется класс SQLAlchemy из Flask SQLAlchemy  - это расширение Flask, которое предоставляет доступ к объекту базы данных SQLAlchemy в приложении Flask
from flask_migrate import Migrate
# Библиотека Flask-Migrate позволяет мигрировать базы данных в приложении Flask, используя SQLAlchemy
from flask_login import login_required
from flask import request, flash, redirect, url_for

app = Flask(__name__)
# создает экземпляр приложения Flask, с именем текущего модуля (__name__ - это встроенная переменная, которая содержит имя текущего модуля)

application = app
# копирует объект приложения Flask в новую переменную `application`. Обычно используется, когда запускается сервер приложений, который ожидает переменную `application` в качестве имени приложения
app.config.from_pyfile('config.py')
# подклюячаем 'config.py', он содержит переменные с параметрами конфигурации, которые могут быть использованы в приложении (настройки базы данных, настройки безопасности, параметры сессии)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# Создание словаря "convention", содержащего соглашение об именовании для различных ограничений таблицы

metadata = MetaData(naming_convention=convention)
# Создание объекта "metadata" класса MetaData, принимающего словарь "convention" в качестве параметра
db = SQLAlchemy(app, metadata=metadata)
#  Создание объекта SQLAlchemy для взаимодействия с базой данных, принимающего объект "app" (Flask-приложение) и объект "metadata" в качестве параметров
migrate = Migrate(app, db)
# Создание объекта "migrate" класса Migrate для выполнения миграций в базе данных, принимающего объект "app" и объект SQLAlchemy "db" в качестве параметров
from models import *
# Чтобы flask_migrate увидел нашу модель, ее надо импортировать

from auth import bp as auth_bp, init_login_manager
app.register_blueprint(auth_bp)

init_login_manager(app)

@app.route('/')
def index():
    return render_template('index.html')

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import Car, Order
from app import db

@app.route('/free_cars')
def free_cars():
    free_cars = Car.query.filter_by(on_duty=True).all()
    return render_template('free_cars.html', free_cars=free_cars)

@app.route('/arrival_time/<car_id>')
@login_required
def arrival_time(car_id):
    car = Car.query.get(car_id)
    if car:
        order = Order.query.filter_by(car=car, passenger=current_user.phone_number).first()
        if order:
            return render_template('arrival_time.html', car=car, order=order)
    flash('Error: Car not found or order not assigned.', 'danger')
    return redirect(url_for('index'))
