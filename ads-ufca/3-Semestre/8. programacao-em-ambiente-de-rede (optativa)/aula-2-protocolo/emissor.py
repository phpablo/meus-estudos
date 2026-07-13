import socket 
import struct
import os
import random
import time

IP_DESTINO = "127.0.0.1"
PORTA_DESTINO = 8080
# NOME_ARQUIVO = "TCC.pdf"
NOME_ARQUIVO = "arquivo_grande.pdf"

TAMANHO_PAYLOAD = 1024
FORMATO_CABECALHO = "!IIB"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(1.0)

tamanho_bytes = os.path.getsize(NOME_ARQUIVO)

trans_id = random.randint(1000,9999)
seq_num = 0

# print(f"[*] Iniciando envio do arquivo {NOME_ARQUIVO}")
print(f"[*] Iniciando envio do arquivo {NOME_ARQUIVO} ({tamanho_bytes / 1024 / 1024:.2f} MB)")
print(f"[*] ID Transação: {trans_id}")

tempo_inicio = time.perf_counter()

with open(NOME_ARQUIVO, "rb") as arquivo:
  while True:
    pedaco = arquivo.read(TAMANHO_PAYLOAD)
    flag = 1 if len(pedaco) < TAMANHO_PAYLOAD or not pedaco else 0

    if not pedaco and flag == 0:
      break

    cabecalho = struct.pack(FORMATO_CABECALHO, seq_num, trans_id, flag)
    pacote_completo = cabecalho + pedaco

    ack_recebido = False
    tentativas = 0
    MAX_TENTATIVAS = 5

    while not ack_recebido and tentativas < MAX_TENTATIVAS:
      try:
        sock.sendto(pacote_completo, (IP_DESTINO, PORTA_DESTINO))
        print(f"[>] Pacote enviado: Seq={seq_num}. Aguardando ACK...(Tentativa {tentativas + 1})")
        ack_pacote, _ = sock.recvfrom(4)
        ack_num = struct.unpack("!I", ack_pacote)[0]

        if ack_num == seq_num:
          print(f"[<] ACK recebido: Seq={ack_num}")
          ack_recebido = True
          seq_num += 1
        else:
          print(f"[-] ACK incorreto recebido")
        
      except socket.timeout:
        print(f"[-] Timeout! Nenhum ACK recebido do pacote Seq={seq_num}.")
        tentativas += 1
    if tentativas == MAX_TENTATIVAS:
      print(f"Limite de retransmissões atingido para o pacote Seq={seq_num}. Abortando envio.")
      break
    if flag == 1:
      print("[*] Último pacote enviado. Finalizando envio.")
      break

tempo_fim = time.perf_counter()
tempo_decorrido = tempo_fim - tempo_inicio

tamanho_bits = tamanho_bytes * 8
megabits = tamanho_bits / 1_000_000
taxa_mbps = megabits / tempo_decorrido

print("\n--- 📊 RESULTADOS DO EXPERIMENTO ---")
print(f"Tempo total: {tempo_decorrido:.4f} segundos")
print(f"Taxa de transferência efetiva: {taxa_mbps:.2f} Mbps")