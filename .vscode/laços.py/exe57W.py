sexo = str(input('digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF': # ENQUANTO VARIAVEL SEXO N SAIR UM VALOR DE F OU M O LAÇO CONTINUA, ENQUANTO SEXO NAO ESTIVER 'FM' WHILE SEXO NOT IN
    sexo = str(input('dados invalidos, informe seu sexo: ')).upper().strip()[0]
print('dado cadastrado com sucesso')