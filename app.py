import sys

clients = ['Alejandro','Edgar']

def add_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
        # _add_coma()
        list_client()
    else:
        print('Client already exist!')


def update_client_name_function(client_name, update_client_name):
    global clients

    if client_name in clients:
        # clients = clients.replace(client_name, update_client_name)
        clients.remove(client_name)
        add_client(update_client_name)
    else:
        print('Client name not in client list!')


def delete_client_function(client_name):
    global clients

    if client_name in clients:
        # clients = clients.replace(client_name, '')
        idx = clients.index(client_name)
        del clients[idx]
    else:
        print('Client name not in client list!')


def search_client(client_name):
    # clients_list = clients.split(',')

    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?  ')

        if client_name == 'exit':
            client_name = None
            break

    if client_name == None:
        sys.exit()

    return client_name


def _add_coma():
    global clients
    clients += ','


def list_client():
    global clients
    print('-*-' * 15)
    print(clients)
    print('-*-' * 15)


def print_welcome():
    print('-*-' * 15)
    print('Welcome to platzi contacts')
    print('What do you want to do?')
    print('[C]reate')
    print('[R]ead')
    print('[U]pdate')
    print('[D]elete')
    print('[S]earch')


if __name__ == '__main__':
    print_welcome()

    command = input('Insert command: ')
    command = command.upper()

    if command == 'C':
        client_name = get_client_name()
        add_client(client_name)
    elif command == 'U':
        client_name = get_client_name()
        update_client_name = input('New name: ')
        update_client_name_function(client_name, update_client_name)
    elif command == 'D':
        client_name = get_client_name()
        delete_client_function(client_name)
        list_client()
    elif command == 'R':
        list_client()
    elif command == 'S':
        client_name = get_client_name()
        search = search_client(client_name)

        if search:
            print('Client is in client list')
        else:
            print(f'The client name {client_name} not in client list')
    else:
        print('Invalid command')
