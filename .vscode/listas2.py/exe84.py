pessoas = []
dados_pessoas = []
pesomax = pesomin = 0
while True:
    dados_pessoas.append(str(input('Nome: ')))
    dados_pessoas.append(int(input('Peso: ')))
    pessoas.append(dados_pessoas)

    for peso in pessoas:
        if peso[1] == max(peso):
            pesomax = max(peso)
            




    
    resp = ' '
    while resp not in 'NS':
        resp = str(input('quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(len(pessoas)) # QUANTIDADE DE PESSOAS CADASTRADASw
print(pesomax)