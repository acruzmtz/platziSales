import csv
from clients.models import Client

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        """ take a class as argument """
        with open(self.table_name, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerow(client.to_dict()) #client reference to a class, not an instance
