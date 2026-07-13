import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('', 5000)

s.bind(server_address)

print("Servidor UDP aguardando mensagem...")

data, client_address = s.recvfrom(1024)

print("Recebido:", data.decode())

MSG = data.decode().upper()

s.sendto(MSG.encode(), client_address)

s.close()
