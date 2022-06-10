pessoas = 0
homem = 0
mulher = 0 
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher +=1
    print('-'*20)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homem} homem cadastrado')
print(f'E temos {mulher} mulheres com menos de 20 anos')

 # RESPOSTA CURSO EM VIDEO


homem = mulher = pessoas = 0
while True:
    idade = int(input('idade: '))
    sexo = ' ' 
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        pessoas += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break    
print(f'total de pessoas com mais de 18 anos: {pessoas}')
print(f'Ao todo temos {homem} homem cadastrado')
print(f'E temos {mulher} mulheres com menos de 20 anos')