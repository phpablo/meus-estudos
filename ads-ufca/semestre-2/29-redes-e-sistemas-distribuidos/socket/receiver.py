import socket, struct
#CONFIG
MULTICAST_GROUP =  '224.3.29.71'
MULTICAST_PORT =  5007
#socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('',MULTICAST_PORT))
#grupo multicast
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4sL',group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)

#receber e exibir mensagens
while True:
    print('Receptor aguardando mensagem')
    data, addr = sock.recvfrom(1024)
    print(f"Recebido de {addr} : {data.decode('utf-8')}")
