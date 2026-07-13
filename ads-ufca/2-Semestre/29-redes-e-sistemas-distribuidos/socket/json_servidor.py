import socket
import json

# config
SERVER_IP = '0.0.0.0'
SERVER_PORT = 12345

# socket
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincular
servidor_socket.bind((SERVER_IP, SERVER_PORT))

# aguardar conexões
servidor_socket.listen(1)
print('Aguardando conexão...')

# aceitar
conexao, endereco = servidor_socket.accept()
print(f'Conectado a {endereco}')

# receber
dados_json = conexao.recv(1024).decode('utf-8')
dados = json.loads(dados_json)

# exibir
print('Dados recebidos:')
print(dados)
print(dados['nome'])
print(dados['idade'])
print(dados['email'])

# fechar tudo
conexao.close()
servidor_socket.close()
