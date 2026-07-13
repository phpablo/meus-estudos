print('-'*30)
print('POR EXTENSO')
print('-'*30)
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  res = int(input('Digite um numero de 0 a 20: '))
  if res not in range(0,21):
    print("Numero inválido!")
    continue
  else:
    print(f'Você digitou o número {extenso[res]}')
    break
