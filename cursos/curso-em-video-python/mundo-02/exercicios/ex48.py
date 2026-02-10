# somar numero inmpares
# multipos de 3
# entre 1 ate 500
count = 0
for i in range(1,501,2):
    if i % 3 == 0:
        count += i  
print(count)