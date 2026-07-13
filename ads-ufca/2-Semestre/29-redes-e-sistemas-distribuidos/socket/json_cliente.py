import socket, json

# dados
usuario = {
    "nome":"Alice",
    "idade":25,
    "email":"gohan@goku.com"
}

# converter dicionario para JSON
usuario_json = json.dumps(usuario)

#config server
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# socket
cliente_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#server
cliente_socket.connect((SERVER_IP,SERVER_PORT))

#enviar json
cliente_socket.send(usuario_json.encode('utf-8'))

#fechar socket
cliente_socket.close()