soma = mil = menor = cont = 0
pbarato = ' '
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        mil += 1
    if cont == 1:
        menor = preco
        pbarato = produto
    else:
       if  preco < menor:
            menor = preco
            pbarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
            break   
print('Fim do Programa')
print(f'O total da compra foi de R${soma} reais')
print(f'Temos o {mil} produtos que custam mais de 1.000 reais')
print(f'O produto mais batato foi {pbarato} com o preço de R${menor} reais')