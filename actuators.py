from flask import Blueprint, render_template, request
from flask_login import login_required

actuators_bp = Blueprint('actuators', __name__, url_prefix='/actuators')

actuators = ['Servo Motor', 'Lâmpada']

@actuators_bp.route('/')
@login_required
def list_actuators():
    global actuators
    return render_template('actuators.html', actuators=actuators)

@actuators_bp.route('/register_actuator')
@login_required
def register_actuator():
    return render_template("register_actuator.html")

@actuators_bp.route('/add_actuator', methods=['GET', 'POST'])
@login_required
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.append(actuator)
    return render_template('actuators.html', actuators=actuators)

@actuators_bp.route('/remove_actuator')
@login_required
def remove_actuator():
    return render_template('remove_actuator.html', actuators=actuators)

@actuators_bp.route('/del_actuator', methods=['GET', 'POST'])
@login_required
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.remove(actuator)
    return render_template("actuators.html", actuators=actuators)
