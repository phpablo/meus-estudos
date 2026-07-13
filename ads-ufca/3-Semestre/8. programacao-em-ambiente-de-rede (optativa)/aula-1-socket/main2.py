import struct

# Vamos empacotar um número de sequência
# (inteiro de 4 bytes) e um flag (1 byte)
seq_num = 1
flag = 255

# Formato:
# '!' significa Network Byte Order (Big-Endian)
# 'I' significa Unsigned Integer (4 bytes)
# 'B' significa Unsigned Char (1 byte)
formato = '!IB'

pacote = struct.pack(formato, seq_num, flag)
print(pacote)
# Saída esperada: b'\x00\x00\x00\x01\xff'
# (Note os 4 bytes para o '1' e o byte final 'ff' que é 255)

# Desempacotando do outro lado
dados_recebidos = struct.unpack(formato, pacote)
print(dados_recebidos)

# Saída esperada: (1, 255)