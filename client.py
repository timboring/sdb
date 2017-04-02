import requests


URI = 'http://localhost:5000/api/v1'


class Client(object):

    def __init__(self, uri=None):
        self.uri = uri or URI

    def get_machines(self):
        response = requests.get('%s/machines' % self.uri).json()
        return response

    def get_machine(self, hostname):
        machine_dict = requests.get(
            '%s/machines/%s' % (self.uri, hostname)).json()
        return machine_dict

    def get_services(self):
        response = requests.get('%s/services' % self.uri).json()
        return response

    def get_service(self, name):
        pass

    def get_networks(self):
        response = requests.get('%s/networks' % self.uri).json()
        return response

    def get_network(self, cidr):
        pass
