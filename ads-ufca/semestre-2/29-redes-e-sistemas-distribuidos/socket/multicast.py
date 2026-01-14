import socket
import struct
import sys

# CONFIGURAÇÕES MULTICAST
MULTICAST_GROUP = '224.3.29.71'
MULTICAST_PORT = 5007

# ---------- EMISSOR ----------
def emissor(nome):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    while True:
        mensagem = input("Digite a mensagem (ou 'sair'): ")

        if mensagem.lower() == "sair":
            print("Encerrando emissor...")
            break

        texto = f"{nome}: {mensagem}"
        sock.sendto(texto.encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))

    sock.close()



# ---------- RECEPTOR ----------
def receptor():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MULTICAST_PORT))

    group = socket.inet_aton(MULTICAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print("Receptor aguardando mensagens multicast...")

    while True:
        data, addr = sock.recvfrom(1024)
        mensagem = data.decode('utf-8')
        print(f"Recebido de {addr}: {mensagem}")

# ---------- SELEÇÃO POR LINHA DE COMANDO ----------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python multicast.py receptor")
        print("  python multicast.py emissor <nome>")
        sys.exit(1)

    modo = sys.argv[1]

    if modo == "emissor":
        if len(sys.argv) < 3:
            print("Erro: informe o nome do usuário")
            print("Exemplo: python multicast.py emissor Ana")
            sys.exit(1)

        nome = sys.argv[2]
        emissor(nome)

    elif modo == "receptor":
        receptor()

    else:
        print("Modo inválido. Use 'emissor' ou 'receptor'.")

