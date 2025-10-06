from flask import Flask, render_template, request, redirect, url_for
from data import users
from login import login, login_manager
from sensors import sensors_bp
from actuators import actuators_bp
from flask_login import login_required, current_user

app = Flask(__name__)
app.secret_key = 'chave_super_secreta_e_segura_experiencia_criativa'

login_manager.init_app(app)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors_bp) 
app.register_blueprint(actuators_bp)

@app.route('/')
def root():
    return redirect(url_for('login.index'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user.id)

# Usuarios

@app.route('/register_user')
@login_required
def register_user():
    return render_template("register_user.html")

@app.route('/add_user', methods=['GET','POST'])
@login_required
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    
    users[user] = password
    print(users)
    return render_template("users.html", devices=users)

@app.route('/list_users')
@login_required
def list_users():
    global users
    return render_template("users.html", devices=users)

@app.route('/remove_user')
@login_required
def remove_user():
    return render_template('remove_user.html', devices=users)

@app.route('/del_user', methods=['GET','POST'])
@login_required
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)

    if user in users:
        users.pop(user)
    return render_template("users.html", devices=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
