from datetime import datetime

from sqlalchemy.dialects import postgresql

from db import db

NETWORK_TYPES = ['IPV4', 'IPV6']


class Error(Exception):
    pass


class NetworkTypeError(Error):
    pass


class Network(db.Model):
    network_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    cidr = db.Column(db.String)
    total_addresses = db.Column(db.Integer)
    used_addresses = db.Column(db.Integer)
    gateway = db.Column(postgresql.INET)


    def __init__(self, cidr, type='IPV4', **kwargs):
        if type not in NETWORK_TYPES:
            raise NetworkTypeError(
                '%s if not a valid network type. Must be one of %s' % (
                    type, NETWORK_TYPES))

        self.type = type
        self.cidr = cidr
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return dict(
            network_id=self.network_id,
            type=self.type,
            cidr=self.cidr,
            total_addresses=self.total_addresses,
            used_addresses=self.used_addresses,
            gateway=self.gateway
        )
