from flask import jsonify
from flask import request
from flask_restful import Resource
from models.service import Service
from models.db import db


class ServiceResource(Resource):

    def get(self, service_id=None):
        if service_id:
            data = Service.query.filter_by(service_id=service_id).first()
            data = data.to_dict()
        else:
            data = Service.query.all()
            data = [service.to_dict() for service in data]
        response = jsonify(data)
        response.status_code = 200
        return response

    def post(self):
        data = request.json
        service = Service(**data)
        db.session.add(service)
        db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return response

    def delete(self):
        pass
