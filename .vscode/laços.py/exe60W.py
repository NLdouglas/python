# resolução com modulo
'''from math import factorial
n = int(input('digite um numero: '))
f = factorial(n)
print('o fatoria de {} é {}'.format(n, f))'''

# forma sem o modulo


n = int(input('digite um numero: '))
c = n
f = 1 # f = 1 pq se for iniciado em zero n ira inicar o laço pois todo numero x 0 é igual 0
print('calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

    