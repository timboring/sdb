import os

from flask import Flask
from flask import jsonify
from flask_restful import Api

from models.db import db
from models.machine import Machine
from models.network import Network
from models.service import Service
from resources.machine import MachineResource
from resources.network import NetworkResource
from resources.service import ServiceResource

API_VERSION = 'v1'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URI', 'postgresql://localhost/sdb')
api = Api(app)
db.init_app(app)
db.app = app

db.create_all()

api.add_resource(MachineResource, '/api/v1/machines', '/api/v1/machines/<int:machine_id>')
api.add_resource(NetworkResource, '/api/v1/networks', '/api/v1/networks/<int:network_id>')
api.add_resource(ServiceResource, '/api/v1/services', '/api/v1/services/<int:service_id>')


@app.route("/")
def index():
    return 'hello'


if __name__ == '__main__':
    app.run()
