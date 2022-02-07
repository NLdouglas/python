maior = 0
menor = 0
for c in range(0, 7):
    ano = int(input('digite o ano de nascimento: '))
    maioridade = 2022 - ano
    if maioridade >= 21:
        maior +=1
    if maioridade < 21:
            menor += 1
print('{} pessoas são maior de idade \n {} pessoas menor de idade'.format(maior, menor))


# outro modo de ser feito 

from datetime import date

atual = date.today().year # importa a data atual 
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('temos {} maiores e {} menores'.format(totmaior, totmenor))