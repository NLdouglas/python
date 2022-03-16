soma = mil = barato = 0
Pbarato = ' '
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    soma += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break   
print(soma)