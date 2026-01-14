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
if __name__ == '__main__':
    user_name = sys.argv[1]
    server(user_name)