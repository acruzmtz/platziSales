clients = 'Alejandro,Edgar,'

def add_client(client_name):
    global clients
    clients += client_name
    _add_coma()
    list_client()


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
    print('-*-' * 15)


if __name__ == '__main__':
    print_welcome()

    
