somaidade = 0
for d in range(1, 5):
    print('{}ª PESSOA'.format(d))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade #todo valor em idade vai pada somaidade
mediaidade = somaidade / 4 
print('a media de idade do grupo é {}'.format(mediaidade))
#verificar media de idade
#homem mais velho
#quantidade de mulheres com menos de 20 anos
