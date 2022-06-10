num = [[], []]
valor = 0 
for c in range(1, 8):
    valor = int(input('digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor) #lista 1
    else:
        num[1].append(valor) #lista 2
print(f'todo os valores {num}')
print(f'valores pares{num[0]}')