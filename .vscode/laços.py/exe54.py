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