import socket,sys
def server(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('', 5000)

    s.bind(server_address)
    s.listen(1)

    print(f'Olá {name} servidor aguardando conexao...')
    conn, address = s.accept()
    message = ''

    data = conn.recv(1024)
    peer_name = data.decode('utf-8')
    conn.sendall(name.encode('utf-8'))

    while message != 'fim':
        data = conn.recv(1024)
        print(f'mensagem recebida de {peer_name}: ', data.decode("utf-8"))
        if not data:
           conn.sendall(data)
        message = input('Digite uma mensagem: ')
        conn.sendall(message.encode('utf-8'))

    conn.close()
    s.close()
def client (name):
    server_address = ('127.0.0.1', 5000)
    message = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server_address)

    print(f'Olá {name}. Começando o chat!')
    s.sendall(name.encode('utf-8'))
    data = s.recv(1024)
    peer_name = data.decode('utf-8')

    while message != 'fim':
        message = input('Digite uma mensagem: ')
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        print(f'mensagem de {peer_name}:', data.decode('utf-8'))
    s.close()

def main(peer_type,user_name):
    if peer_type == 'servidor':
        server(user_name)
    if peer_type == 'cliente':
        client(user_name)
if __name__ == '__main__':
    peer_type = sys.argv[1]
    user_name = sys.argv[2]
    main(peer_type,user_name)