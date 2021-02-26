import csv
from clients.models import Client
import os

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        """ take a class as argument """
        with open(self.table_name, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerow(client.to_dict()) #client reference to a class, not an instance

    def list_clients(self):
        with open(self.table_name, mode='r') as file:
            reader = csv.DictReader(file, fieldnames=Client.schema())

            return list(reader)

    def update_client(self, updated_client):
        """ take a class as parameter and compare with a uid client in the list """
        clients = self.list_clients()

        #new list to save all clients
        updated_clients = []

        for client in clients:
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)

        # finally, save all clients again
        self._save_clients_to_disk(updated_clients)


    def _save_clients_to_disk(self, clients):
        # create a temporal table
        tmp_table_name = self.table_name + '.tmp'

        with open(tmp_table_name, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
