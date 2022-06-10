r = 'SN'
cont = soma = menor = maior = 0
while r != "N":
    num = int(input('digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    r = input('quer continuar [S/N]: ').upper().strip()[0]
media = soma / cont 
print('Voce digitou {} números e a médio foi {:.2f}'.format(cont, media))
print('o maior valor foi {} e o menor valor foi {}'.format(maior, menor))