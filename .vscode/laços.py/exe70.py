total = mil = menor = cont = 0
pbarato = ' '

while True:
    produto = input('Nome do produto:  ')
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        mil += 1
    if cont == 1:
        menor = preco
        pbarato = produto
    else:
        if preco < menor:
            menor = preco
            pbarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(total)
print(mil)
print(f'{pbarato} e {menor}')

