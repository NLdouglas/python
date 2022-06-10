num = int(input('digite um numero: '))
tot = 0
for c in range(1, num + 1):  # se o input for 4 o laço for conta ate 3 por isso o +1 assim dando a saida correta
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1 # mesma coisa q tot = +1 
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n \033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('é primo')
else:
    print('nao é primo')