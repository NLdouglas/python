from random import randint
#laço pra ler a saida e entrada do usuario
palpite = int(input('digite um numero de 0 a 10: '))
maquina = randint(0, 10)
cont = 0
while palpite != maquina:
    cont += 1
    palpite = int(input('seu palpite foi {} e da maquina foi {}, tente novamente: '.format(palpite, maquina)))
    if pal
#contador dos palpites 