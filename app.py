clients = 'Alejandro,Edgar,'

def add_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        _add_coma()
        list_client()
    else:
        print('Client already exist!')


def update_client_name_function(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name, update_client_name)
    else:
        print('Client name not in client list!')


def get_client_name():
    return input('What is the client name?  ')


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
    print('[U]pdate')


if __name__ == '__main__':
    print_welcome()

    command = input('Insert command: ')

    if command == 'C':
        client_name = get_client_name()
        add_client(client_name)
        list_client()
    elif command == 'U':
        client_name = get_client_name()
        update_client_name = input('New name: ')
        update_client_name_function(client_name, update_client_name)
        list_client()
    else:
        pass

    
