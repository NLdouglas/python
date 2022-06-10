#ceil = arredondamento para cima 
#floor = arredodamento para baixo
#trunc = elimina da , para frente 
#pow = calculo de potencia
#sqrt = raiz quadrada   
#factorial = calculo de fatorial
#funçoes da lib math

from math import sqrt, floor
#import math
num = int(input('digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} é {:.2f}'.format(num, floor(raiz)))

#import random
#num = random.randint(1, 10) = numero inteiro aleatorio de 1 a 10