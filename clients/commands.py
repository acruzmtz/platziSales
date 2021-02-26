import click
from clients.services import ClientService
from clients.models import Client
from tabulate import tabulate

@click.group()
def clients():
    """ Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client name')
@click.option('-e', '--email', type=str, prompt=True, help='The client name')
@click.option('-p', '--position', type=str, prompt=True, help='The client name')
@click.pass_context
def create(context, name, company, email, position):
    """ Create a new client """
    client = Client(name, company, email, position)
    client_service = ClientService(context.obj['clients_table'])
    client_service.create_client(client) # pass a class as parameter


@clients.command()
@click.pass_context
def list(context):
    """ List all clients """
    client_service = ClientService(context.obj['clients_table'])
    clients = client_service.list_clients()

    # format table
    headers = [field.capitalize() for field in Client.schema()]
    table = []

    # click.echo('| Name    | Company   | Email    | Position     | ID')
    # click.echo('*' * 50)
    for client in clients:
        #click.echo('{}   | {}    | {}   | {}    | {}'.format(client['name'], client['company'], client['email'], client['position'], client['uid']))
        table.append([client['name'], client['company'], client['email'], client['position'], client['uid']])

    click.echo(tabulate(table, headers))


@clients.command()
@click.pass_context
def update(context, username):
    """ Update client info """
    pass


@clients.command()
@click.pass_context
def delete(context, username):
    """ Delete a client """
    pass


all = clients
