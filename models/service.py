from datetime import datetime

from sqlalchemy.dialects import postgresql

from db import db
from db import machine_services


class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    cicd_home = db.Column(db.String)
    doc_home = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    machine_services = db.relationship(
        'Machine',
        secondary=machine_services,
        backref=db.backref('services', cascade='all'),
        cascade='save-update, merge')

    def __init__(self, name, machines=None, **kwargs):
        self.name = name
        self.machines = machines
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.cicd_home = kwargs.get('cicd_home')
        self.doc_home = kwargs.get('doc_home')

    def to_dict(self):
        return dict(
            service_id=self.service_id,
            name=self.name,
            cicd_home=self.cicd_home,
            doc_home=self.doc_home,
            machines=[m.hostname for m in self.machine_services]
        )
