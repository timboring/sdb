import os

from flask import Flask
from flask import jsonify
from flask_restful import Api

from models.db import db
from models.machine import Machine
from models.network import Network
from resources.machine import MachineResource

API_VERSION = 'v1'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URI', 'postgresql://localhost/sdb')
api = Api(app)
db.init_app(app)
db.app = app

db.create_all()

api.add_resource(MachineResource, '/api/v1/machines', '/api/v1/machines/<int:machine_id>')


@app.route("/")
def index():
    return 'hello'


if __name__ == '__main__':
    app.run()
