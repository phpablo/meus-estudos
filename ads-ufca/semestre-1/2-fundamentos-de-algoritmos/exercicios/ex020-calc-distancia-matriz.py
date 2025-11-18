ls = [

]
while True:
    x = int(input('Digite um número inteiro:\n'))
    if x == 0:
        break
    ls.append(x)
maior_dist = 0
n = len(ls)
for i in range(0,n):
    dist = ls[i] - ls[n-1]
    if dist < 0:
        dist = -dist
    if dist > maior_dist:
        maior_dist = dist
print(maior_dist)

