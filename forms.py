from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError,DataRequired,EqualTo
from models import User

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя: ')
    password = PasswordField('Пароль: ')
    remember_me = BooleanField('Запомнить меня:')
    submit = SubmitField('Войти:')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя: ', validators=[DataRequired()])
    email = StringField('Имя пользователя: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ',validators=[DataRequired()])
    password_again = PasswordField('Пароль (подтверждение): ',
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def check_username(self, username):
        user = User.query.filter_by(username=username.data)
        if user is not None:
            raise ValidationError('Полозователь с таким ником уже зарегистрирован ')

    def check_email(self, email):
        user = User.query.filter_by(email=email.data)
        if user is not None:
            raise ValidationError('Полозователь с такой почтой уже зарегистрирован ')