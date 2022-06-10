matriz = [[0,0,0], [0,0,0], [0,0,0]]
somp = sterc = mai = 0
for l in range(0, 3): # numero de linhas
    for c in range(0, 3): # numero de colunas
        matriz[l] [c] = int(input(f'digite um valor para {l}, {c}: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end=' ') #mostra os valores digitados nas suas respcetivas listas
        if matriz[l] [c] %2 == 0:
            somp += matriz[l] [c]
    print()
print(somp)
for l in range(0, 3):
    sterc += matriz[l][2] # coluna sempre fixa oq varia é a linha 
print(sterc)
for c in range(0, 3):
    if c == 0:
        mai = matriz[1] [c]
    elif matriz[1] [c] > mai:
        mai = matriz[1] [c]
print(mai)