from flask import jsonify
from flask import request
from flask_restful import Resource
from models.machine import Machine
from models.db import db


class MachineResource(Resource):

    def get(self, machine_id=None):
        service_name = request.args.get('service')
        if service_name:
            data = Machine.query.filter(
                Machine.services.any(name=service_name)).all()
            data = [machine.hostname for machine in data]
        elif machine_id:
            data = Machine.query.filter_by(machine_id=machine_id).first()
            data = data.to_dict()
        else:
            data = Machine.query.all()
            data = [machine.to_dict() for machine in data]
        response = jsonify(data)
        response.status_code = 200
        return response

    def post(self):
        data = request.json
        machine = Machine(**data)
        db.session.add(machine)
        db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return response

    def delete(self):
        pass
