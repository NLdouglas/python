# resolução com modulo
from math import factorial
n = int(input('digite um numero: '))
f = factorial(n)
print('o fatoria de {} é {}'.format(n, f))

# forma sem o modulo

n = int(input('digite um numero: '))
c = n
f = 1 # f = 1 devido a multiplicação sendo todo n mult por 0 = 0 assim n iniciando o laço
print('calculando {}! ='.format(n), end='')
while c >0:
    print('{}'.format(c), end='')
    print('x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
