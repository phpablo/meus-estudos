import socket, struct

MULTICAST_GROUP =  '224.3.29.71'
MULTICAST_PORT =  5007

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

ttl = struct.pack('b',1)

sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)

sock.sendto(f"Olá, grupo multicast!".encode('utf-8'),(MULTICAST_GROUP,MULTICAST_PORT))
