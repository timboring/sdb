from flask import jsonify
from flask import request
from flask_restful import Resource
from models.machine import Machine
from models.service import Service
from models.db import db
import pdb

class Error(Exception):
    pass


class MachineDoesNotExistError(Error):
    pass


class MachinesCannotBeNoneError(Error):
    pass


class ServiceResource(Resource):

    def get(self, service_id=None):
        name = request.args.get('name')
        if name:
            data = Service.query.filter_by(name=name).first()
            data = data.to_dict()
        if service_id:
            data = Service.query.filter_by(service_id=service_id).first()
            data = data.to_dict()
        else:
            data = Service.query.all()
            data = [service.to_dict() for service in data]
        response = jsonify(data)
        response.status_code = 200
        return response

    def _get_machines(self, machine_list):
        machines = []
        for machine in machine_list:
            m = Machine.query.filter_by(hostname=machine).first()
            if not m:
                raise MachineDoesNotExistError(
                    '%s does not exist. Please add machine first.' % machine)
            machines.append(m)
        return machines

    def post(self):
        data = request.json
        machine_list = data.get('machines')
        if machine_list:
            machines = self._get_machines(machine_list)
        else:
            raise MachinesCannotBeNoneError(
                'A service must have 1 or more machines.')
        service = Service(**data)
        for machine in machines:
            service.machines.append(machine)
        db.session.add(service)
        db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return response

    def delete(self, service_id):
        if service_id:
            service = Service.query.filter_by(service_id=service_id).first()
            service.machines = []
            db.session.commit()
            db.session.delete(service)
            db.session.commit()
        response = jsonify({})
        response.status_code = 201
        return response
