#cliente
import socket

server_address = ('127.0.0.1', 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

MSG = 'Primeira mensagem em rede'

s.sendto(MSG.encode(), server_address)

data, _ = s.recvfrom(1024)

print(data.decode())

s.close()
