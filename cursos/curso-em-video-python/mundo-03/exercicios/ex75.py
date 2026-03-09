from random import randint
print('-'*30)
print('Analise valores')
print('-'*30)

list_of_numbers = []
list_of_even_numbers = []
count = 0
count_nine = 0
first_tree = 1
is_true = False
while count < 4:
  try:
    num = int(input('Digite um número: '))
    list_of_numbers.append(num)
    if num == 9:
      count_nine += 1
    if not is_true and num == 3:
      first_tree = count
      is_true = True
    if num % 2 == 0:
      list_of_even_numbers.append(num)
    count += 1
  except ValueError:
    print('EU DISSE NUMERO')
# ler 4 valor do teclado e colocar em uma tupla
tupla_of_numbers = (list_of_numbers)

# quantas vezes apareceu o 9
print(f'O número 9 apareceu {count_nine} vezes')
# em que posição foi digitado o primeiro valor 3
print(f'O número 3 está na {first_tree}ª posição')
# quais numeros pares
print(f'A quantidade de números pares é {len(list_of_even_numbers)}')

