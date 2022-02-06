
homem = 0
nomevelho = ''
qntdmulher = 0
somaidade = 0 # variavel criada para acumular os valores de idade
for d in range(1, 5):
    print('{}ª PESSOA'.format(d))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    somaidade += idade #todo valor em idade vai pada somaidade
    if sexo == 'M':
        if idade == 1:
            homem = idade 
            idade = homem
            nomevelho = nome
        else:
            if idade > homem:
                homem = idade
                nomevelho = nome
    if sexo == 'F' and idade < 20:
        qntdmulher += 1
        
        


mediaidade = somaidade / 4 #pega todas as idades e divide por 4 assim fazendo a media 
print('a media de idade do grupo é {:.2f}'.format(mediaidade))
print('o nome do homem mais velho é {}'.format(nomevelho))
print('quantidade de mulher com menos de 20 anos de idade é {}'.format(qntdmulher))


