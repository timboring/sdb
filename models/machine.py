from datetime import datetime

from sqlalchemy.dialects import postgresql

from operating_systems import OperatingSystems
from db import db
from db import machine_services


class Machine(db.Model):
    machine_id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    # (TODO): consider using Postgres' INET[] type
    ip_addresses = db.Column(postgresql.ARRAY(db.String))
    net_interfaces = db.Column(postgresql.ARRAY(db.String))
    operating_system = db.Column(db.Enum(OperatingSystems))
    disk = db.Column(db.Integer)
    ram = db.Column(db.Integer)
    cores = db.Column(db.Integer)
    manufacturer = db.Column(db.String)
    model = db.Column(db.String)
    machine_services = db.relationship(
        'Service',
        secondary=machine_services,
        backref='machines',
        cascade='save-update, merge, delete')

    def __init__(self, hostname, **kwargs):
        self.hostname = hostname
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.ip_addresses = kwargs.get('ip_addresses')
        self.net_interfaces = kwargs.get('net_interfaces')
        self.disk = kwargs.get('disk')
        self.ram = kwargs.get('ram')
        self.cores = kwargs.get('cores')
        self.manufacturer = kwargs.get('manufacturer')
        self.model = kwargs.get('model')

    def to_dict(self):
        return dict(
            machine_id=self.machine_id,
            hostname=self.hostname,
            ip_addresses=self.ip_addresses,
            net_interfaces=self.net_interfaces,
        )
