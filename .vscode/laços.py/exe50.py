s = 0
cont = 0 
for n in range(0, 6):
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        s += num
        cont += 1
print('quantidade de n pares {} e a soma {} '.format(cont, s))