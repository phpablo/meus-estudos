import socket

server_address = ('127.0.0.1', 5000)

MSG = 'Primeira mensagem em rede'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# s.connect(server_address)

s.sendto(str.encode(MSG), server_address)

data,_ = s.recvfrom(1024)

print(data)

s.close()