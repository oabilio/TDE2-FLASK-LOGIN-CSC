from flask import Blueprint, render_template, request
from flask_login import login_required

sensors_bp = Blueprint('sensors', __name__, url_prefix='/sensors')

sensors = ['Umidade', 'Temperatura', 'Luminosidade']

@sensors_bp.route('/')
@login_required
def list_sensors():
    global sensors
    return render_template('sensors.html', sensors=sensors)

@sensors_bp.route('/register_sensor')
@login_required
def register_sensor():
    return render_template("register_sensor.html")

@sensors_bp.route('/add_sensor', methods=['GET', 'POST'])
@login_required
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.append(sensor)
    return render_template('sensors.html', sensors=sensors)

@sensors_bp.route('/remove_sensor')
@login_required
def remove_sensor():
    return render_template('remove_sensor.html', sensors=sensors)

@sensors_bp.route('/del_sensor', methods=['GET', 'POST'])
@login_required
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.remove(sensor)
    return render_template("sensors.html", sensors=sensors)
