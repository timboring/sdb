#!/usr/local/bin/python

import requests
import time

machine_uri = 'http://localhost/api/v1/machines'
service_uri = 'http://localhost/api/v1/services'


# Create 1000 machines
#created = 0
#host_prefix = 'test-machine-%s.example.com'
#
#count = 1
#while count <= 1000:
#    r = requests.post(
#        'http://localhost:5000/api/v1/machines',
#        json = {
#            'hostname': host_prefix % count,
#            'disk': 100,
#            'ram': 1024,
#            'cores': 24
#        })
#    count += 1
#    if (count % 10) == 0:
#        print 'Sleeping for 1 second'
#        time.sleep(1)


# Create 20 services
service_prefix = 'dummy-service-%s'
count = 1
while count <= 10:
    machines = []
    if count % 2 == 0:
        machines = ['test-machine-%s.example.com' % num for num in range(1, 5)]
    else:
        machines = ['test-machine-%s.example.com' % num for num in range(500, 520)]
    r = requests.post(
        'http://localhost:5000/api/v1/services',
        json = {
            'name': service_prefix % count,
            'machines': machines
        })
    count += 1


