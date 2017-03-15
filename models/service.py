from datetime import datetime

from sqlalchemy.dialects import postgresql

from db import db
from db import machine_services


class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # TODO(tjb): add relationship to machines
    machines = db.relationship('Machine', backref='service')
    machine_id = db.Column(db.Integer, db.ForeignKey('machine.machine_id'))
    machine_services = db.relationship(
        'Machine',
        secondary=machine_services,
        backref='services',
        cascade='save-update, merge, delete')

    def __init__(self, name, machines=None):
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.machines = machines

    def add_machine(self, machine):
        self.machines.append(machine)

    def to_dict(self):
        return dict(
            service_id=self.service_id,
            name=self.name,
            machines=[m.to_dict() for m in self.machines]
        )
