import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('', 5000)

s.bind(server_address)

# s.listen(1)

# conn, address = s.accept()

data, client_address = s.recvfrom(1024)

if not data:
   s.sendto(data)

MSG = data.decode().upper()

s.sendto(str.encode(MSG),client_address)

s.close()