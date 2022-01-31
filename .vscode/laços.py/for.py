'''for c in range(1, 6):
    print('oi')
print('fim')'''

for c in range(6, 0, -1): # -1 no final se como iteração (oq acontece no final do laço)
    print(c)
print('fim')

i = int(input('inicio: ')) #numento inicial
f = int(input('fim: '))     # numero inicial +1 ate o numro final, ou seja, vai somando de 1 em 1 ate o numero final
p = int(input('passo: ')) # se numero passo for 3 sera a conta inicial ate o fim pulando de 3 em 3 
for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0, 4):
    n = int(input('digite um valor: '))
    s += n 
print('a soma entre os numeros é {}'.format(s))