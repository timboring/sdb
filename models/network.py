from datetime import datetime

from sqlalchemy.dialects import postgresql

from db import db
from network_types import NetworkTypes


class Network(db.Model):
    network_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(NetworkTypes))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    cidr = db.Column(db.String)
    total_addresses = db.Column(db.Integer)
    used_addresses = db.Column(db.Integer)
    gateway = db.Column(postgresql.INET)


    def __init__(self, type, cidr, **kwargs):
        self.type = type
        self.cidr = cidr
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
