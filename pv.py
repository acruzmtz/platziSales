import click
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(context):
    context.obj = {}
    context.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
