from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

machine_services = db.Table(
    'machine_services',
    db.Column('machine_id', db.Integer, db.ForeignKey('machine.machine_id')),
    db.Column('service_id', db.Integer, db.ForeignKey('service.service_id'))
)
