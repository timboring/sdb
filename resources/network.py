from flask import jsonify
from flask import request
from flask_restful import Resource
from models.network import Network
from models.db import db


class NetworkResource(Resource):

    def get(self, network_id=None):
        if network_id:
            data = Network.query.filter_by(network_id=network_id).first()
            data = data.to_dict()
        else:
            data = Network.query.all()
            data = [network.to_dict() for network in data]
        response = jsonify(data)
        response.status_code = 200
        return response

    def post(self):
        data = request.json
        network = Network(**data)
        db.session.add(network)
        db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return response

    def delete(self):
        pass
