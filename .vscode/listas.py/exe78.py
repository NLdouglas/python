
lista = []
for n in range(0, 5):
    num = int(input(f'digite um valor para a posição {n}: '))
    lista.append(num)
print(f'Voce digitou os valores {lista}')
print(f'o maior valor foi {max(lista)} nas posições ', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end=' ')
print()
print(f'O menor valor foi {min(lista)} nas posições ', end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end=' ')
print()