from datetime import datetime

from sqlalchemy.dialects import postgresql

from db import db
from db import machine_services


class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    machine_services = db.relationship(
        'Machine',
        secondary=machine_services,
        backref='services',
        cascade='save-update, merge, delete')

    def __init__(self, name, machines=None):
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return dict(
            service_id=self.service_id,
            name=self.name,
            machines=[m.hostname for m in self.machine_services]
        )
