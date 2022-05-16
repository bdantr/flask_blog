from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app import app, login
from forms import LoginForm
from models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))



@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('main_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)
        if user is None or not User.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main_page'))
    return render_template('login.html', title='Login page', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))