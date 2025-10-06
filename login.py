from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from data import users

login = Blueprint("login", __name__, template_folder="templates")

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    def get_id(self):
        return self.id

login_manager = LoginManager()
login_manager.login_view = 'login.index'

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Rotas

@login.route('/login', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        if user in users and users[user] == password:
            user_obj = User(user)
            login_user(user_obj)
            return redirect(url_for('home'))
        else:
            return '<h1>informaçoes erradas...</h1>'
    return render_template('login.html')

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))