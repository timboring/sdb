from flask_script import Manager
from flask_script import Shell
from flask_sqlalchemy import get_debug_queries
from pprint import pprint

from models.machine import Machine
from models.network import Network
from models.service import Service
from models.db import db
import client

from api import app

manager = Manager(app)

def make_shell_context():
    return dict(
        app=app,
        db=db,
        pprint=pprint,
        gq=get_debug_queries,
        Machine=Machine,
        Network=Network,
	    Service=Service,
        client=client
    )

manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
