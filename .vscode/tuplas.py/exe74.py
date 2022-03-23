#gerador de numeros aleatorios
'''from random import randint
cont = menor = maior = 0
for n in range(0, 5):
    num = (randint(0, 9))
    cont += 1
    
    #menor numero
    if cont == 1:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
#maior numero
    print(f'{num}', end=' ')
print(f'\nO menor numero é {menor}')
print(f'O maior numero é {maior}')
'''
# CURSO EM VIDEO

from random import randint
num = (randint(0, 10), randint(0, 10), randint(1, 10), randint(1, 10), 
randint(1, 10))

print(f'Os numeros sorteados foram {num}')
print(f'O menor numero foi {min(num)}')
print(f'O maior numero foi {max(num)}')