from flask import Flask, Blueprint, current_app
from threading import Thread
from sensors import Sensors

bp = Blueprint('metrics', __name__)

@bp.route('/metrics', methods=['GET'])
def metrics():
    metrics = [{
        'name': 'hygrometer',
        'value': current_app.sensors.humidity.value
    }, {
        'name': 'temperature',
        'value': current_app.sensors.temperature.value
    }, {
        'name': 'light',
        'value': current_app.sensors.light.value
    }]
    out = ''
    for metric in metrics:
        out += "sensors{name=\"%s\"} %s\n" % (metric['name'], metric['value'])
    return out


def create_app():
    app = Flask(__name__)
    app.sensors = Sensors()
    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.sensors.start()
    app.run(port=5000)