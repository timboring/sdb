#!/usr/local/bin/python

import requests
import time

machine_uri = 'http://localhost/api/v1/machines'
service_uri = 'http://localhost/api/v1/services'


# Create 1000 machines
created = 0
host_prefix = 'test-machine-%s.example.com'

count = 0
while created < 10:
    machine_num = 1
    import pdb;pdb.set_trace()
    r = requests.post(
        'http://localhost:5000/api/v1/machines',
        json = {
            'hostname': host_prefix % machine_num,
            'disk': 100,
            'ram': 1024,
            'cores': 24
        })
    machine_num += 1
    count += 1
    if count == 10:
        time.sleep(1)


# Create 20 services
