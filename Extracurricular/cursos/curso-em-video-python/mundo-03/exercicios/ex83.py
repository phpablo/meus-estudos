'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expr = str(input('Digite uma expressão: ')).strip()
pilha = list()
for simb in expr:
    if simb == '(':
      pilha.append('(')
    elif simb == ')':
      if len(pilha) > 0:
        pilha.pop()
      else:
        pilha.append(')')
        break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')





'''
while True:
  exp = str(input('Digite uma expressão: ')).strip()
  pilha1 = list()
  pilha2 = list()
  for simb in exp:
    if simb == '(':
      pilha1.append('(')
    elif simb == ')':
      pilha2.append(')')

  if len(pilha1) == len(pilha2):
    print('Expressão válida!')
  else:
    print('Expressão inválida!')
  break
'''
