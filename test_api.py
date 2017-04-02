import pdb
import unittest

from api import app, db
from models.machine import Machine
from models.service import Service


TEST_MACHINE = {
    'hostname': 'foo.example.com',
    'ip_addresses': None,
    'machine_id': None,
    'net_interfaces': None,
    'disk': None,
    'ram': None,
    'cores': None,
    'services': []
}


class BaseTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/testing'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestMachineModel(BaseTest):

    def test_create_machine(self):
        mach = Machine(
            'foo.example.com',
            ip_addresses=['192.168.1.100, 192.168.2.100'],
            net_interfaces=['eth0', 'eth1'],
            disk=100,
            ram=2048,
            cores=4)
        db.session.add(mach)
        db.session.commit()
        self.assertEqual(1, mach.machine_id)

    def test_todict_returns_dict(self):
        mach = Machine('foo.example.com')
        self.assertEqual(TEST_MACHINE, mach.to_dict())


class TestMachineResource(BaseTest):
    pass


class TestServiceModel(BaseTest):

    def setUp(self):
        super(TestService, self).setUp()
        self.machine1 = Machine('foo1.example.com')
        self.machine2 = Machine('foo2.example.com')

    def test_create_service(self):
        foo_service = Service(
            'foo', machines=[self.machine1, self.machine2]
        )
        db.session.add(foo_service)
        db.session.commit()
        self.assertEqual(1, foo_service.service_id)
        self.assertEqual(2, len(foo_service.machines))

    def test_create_service_with_nonexisting_machines(self):
        self.assertRaises(AttributeError, Service, 'foo', machines=['foo.example.com'])

    def test_create_service_with_no_machines(self):
        self.assertRaises(TypeError, Service, 'foo')


if __name__ == '__main__':
    unittest.main()
