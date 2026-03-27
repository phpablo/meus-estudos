def just_a(list):
  for i in list:
    if 'a' in i.lower():
      print(i)

list = ['banana', 'abacaxi', 'uva', 'pera', 'manga','Kiwi','Quejio']
try:
  print('Lista completa:', list)
  just_a(list)
except Exception as e:
  print('Ocorreu um erro:', e)