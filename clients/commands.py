import click

@click.group()
def clients():
    """ Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(context, name, company, email, position):
    """ Create a new client """
    pass


@clients.command()
@click.pass_context
def list(context):
    """ List all clients """
    pass


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
