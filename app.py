import sys

clients = [
    {
        'name': 'Alejandro',
        'company': 'breakfood',
        'email': 'acruzmtz@gmail.com',
        'position': 'Back-end developer'
    },
    {
        'name': 'Edgar',
        'company': 'breakfood',
        'email': 'ed@gmail.com',
        'position': 'Front-end developer'
    }
]

def add_client(client):
    global clients

    if client not in clients:
        clients.append(client)
        list_client()
    else:
        print('Client already exist!')


def update_client_name_function(idx, update_client):
    global clients

    del clients[idx]
    clients.append(update_client)
    list_client()


def check_if_client_exist(client_name):
    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            return idx


def delete_client_function(client_name):
    global clients

    idx = check_if_client_exist(client_name)

    if idx != None:
        del clients[idx]
        list_client()
    else:
        print('Client name not in client list!')


def search_client(client_name):

    idx = check_if_client_exist(client_name)

    if idx != None:
        info_client = clients[idx]
        print(info_client['name'])
        print(info_client['company'])
        print(info_client['email'])
        print(info_client['position'])
    else:
        print(f'The client name {client_name} not in client list')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}?')

    return field


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


def list_client():
    for idx, client in enumerate(clients):
        print('-*-' * 15)
        print('Name: ',client['name'])
        print('Company: ',client['company'])
        print('Email: ',client['email'])
        print('Position: ',client['position'])
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
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }

        add_client(client)
    elif command == 'U':
        client_name = get_client_name()

        idx = check_if_client_exist(client_name)

        if idx != None:
            update_client = {
                'name': _get_client_field('name'),
                'company': _get_client_field('company'),
                'email': _get_client_field('email'),
                'position': _get_client_field('position')
            }

            update_client_name_function(idx, update_client)
        else:
            print('Client name not in client list!')

    elif command == 'D':
        client_name = get_client_name()
        delete_client_function(client_name)
    elif command == 'R':
        list_client()
    elif command == 'S':
        client_name = get_client_name()
        search = search_client(client_name)
    else:
        print('Invalid command')
