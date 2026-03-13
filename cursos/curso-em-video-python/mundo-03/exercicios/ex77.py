from random import randint
print('-'*30)
print("VOGAIS".center(30))
print('-'*30)
words = ('arroz','feijao','carne','bife acebolado','batata frita','pizza','hamburguer')
vogal = []
for word in words:
  for char in word:
    if char in "aeiou":
      vogal.append(char)
  print(word)
  print(vogal)
  vogal = []
