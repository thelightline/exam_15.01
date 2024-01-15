from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
from app import db
from models import User

def load_user(user_id):
    user = User.query.get(user_id)
    return user

# Функция "init_login_manager" создает и настраивает объект "login_manager" класса "LoginManager"
# для управления аутентификацией пользователей в приложении Flask
def init_login_manager(app):
	login_manager = LoginManager()
	# Создан экземпляр класса
	login_manager.init_app(app)
	# Даем приложению знать о существования логин менеджера
	login_manager.login_view = 'auth.login'
	login_manager.login_message = 'Для выполнения данного действия необходимо пройти процедуру аутентификации.'
	login_manager.login_message_category = 'warning'
	# функция "load_user" будет вызвана при каждой следующей авторизации пользователя,
	#  чтобы получить информацию о пользователе из базы данных или источника данных
	login_manager.user_loader(load_user)

# Создается объект "bp" типа Blueprint для модуля "auth" в приложении Flask с именем "name".
#  При обращении к маршрутам модуля "auth", они будут иметь префикс "/auth".
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        user = User.query.filter_by(phone_number=phone_number).first()

        if user:
            sms_code = randint(1000, 9999)  # Генерация случайного SMS-кода
            user.sms_code = generate_password_hash(str(sms_code))  # Хешируем SMS-код и сохраняем в базу данных
            db.session.commit()

            # Отправка SMS-кода (здесь должна быть ваша логика отправки СМС)

            return redirect(url_for('auth.verify_sms', user_id=user.id))
        else:
            flash('Phone number not found.', 'danger')

    return render_template('login.html')

@bp.route('/verify_sms/<int:user_id>', methods=['GET', 'POST'])
def verify_sms(user_id):
    user = User.query.get(user_id)

    if not user:
        flash('User not found.', 'danger')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        entered_code = request.form.get('sms_code')

        if check_password_hash(user.sms_code, entered_code):
            # SMS-код верен, производим авторизацию пользователя
            login_user(user)
            flash('You have been successfully authenticated.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid SMS code. Please try again.', 'danger')

    return render_template('verify_sms.html', user=user)

