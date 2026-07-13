list_num = []
mai = 0
men = 0

for c in range(0,5):
    list_num.append(int(input(f'Digite um valor na posição {c}: ')))

    if c == 0:
        mai = men = list_num[c]
    else:
        if list_num[c] > mai:
            mai = list_num[c]
        if list_num[c] < men:
            men = list_num[c]

print('=-'*30)
print(f'Você digitou os valors {list_num}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(list_num):
    if v == mai:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i,v in enumerate(list_num):
    if v == men:
        print(f'{i}...', end='')
print()