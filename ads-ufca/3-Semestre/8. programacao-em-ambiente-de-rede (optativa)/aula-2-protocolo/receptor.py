import socket 
import struct
import os
import random

IP = ""
PORTA = 8080
FORMATO_CABECALHO = "!IIB"
TAMANHO_CABECALHO = struct.calcsize(FORMATO_CABECALHO)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORTA))
print(f"Servidor UDP aguardando arquivos em {IP}:{PORTA}")
sock.settimeout(10.0)


seq_esperado = 0
arquivos_destino = open("recebido.pdf", "wb")
transacao_atual = None

try:
  while True:
    try:
      if random.random() < 0.3:
        print("[!] Simulando perda de pacote. Ignorando pacote recebido.")
        sock.recvfrom(2048)
        continue
        # pass
      pacote, endereco_cliente = sock.recvfrom(2048)
      cabecalho_bytes = pacote[:TAMANHO_CABECALHO]
      payload = pacote[TAMANHO_CABECALHO:]

      seq_num, trans_id, flag = struct.unpack(FORMATO_CABECALHO, cabecalho_bytes)

      if transacao_atual is None:
        transacao_atual = trans_id

      if trans_id != transacao_atual:
        continue
      
      if seq_num == seq_esperado:
        print(f"[+] Pacote recebido: Seq={seq_num}. Gravando no disco.")
        arquivos_destino.write(payload)
        seq_esperado += 1

        ack_pacote = struct.pack("!I", seq_num)
        sock.sendto(ack_pacote, endereco_cliente)

        if flag == 1:
          print("[*] Ultimo pacote recebido. Finalizando a transação.")
          arquivos_destino.close()
          break
      else:
        print(f"[-] Pacote fora de ordem ou duplicado! Recebido: Seq={seq_num}, Esperado: {seq_esperado}")
        if seq_esperado > 0:
            seq_anterior = seq_esperado - 1
            ack_pacote = struct.pack("!I", seq_anterior)
            sock.sendto(ack_pacote, endereco_cliente)
            print(f"[*] Reenviando ACK do pacote anterior: Seq={seq_anterior}")
    except socket.timeout:
      print("\n[*] Timeout! O cliente sumiu por mais de 10 segundos. Abortando transação...")
      arquivos_destino.close()
      if os.path.exists('recebido.pdf'):
        os.remove('recebido.pdf')
        print("[*] Rollback executado: Arquivo incompleto removido com sucesso!")
      break
    
except KeyboardInterrupt:
  print("\n[*]Servidor encerrado.")
  arquivos_destino.close()





