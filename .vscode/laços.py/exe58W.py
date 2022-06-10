#MINHA SOLUÇÃO
from random import randint
#laço pra ler a saida e entrada do usuario
palpite = int(input('digite um numero de 0 a 10: '))
maquina = randint(0, 10)
cont = 0
while palpite != maquina:
    cont += 1
    palpite = int(input('seu palpite foi {} o da maquina foi outro, tente novamente: '.format(palpite, maquina)))
    if palpite == maquina:
        cont += 1
        print('Parabens voce jogou o mesmo numero q a maquina {}, foram {} tentativas'.format(palpite,cont))
#contador dos palpite

#VERSAO CURSO EM VIDEO

from random import randint

computador = randint(0, 10)
print('sou seu computador..Acabei de pensar em numero entre 0 e 10')
print('sera que voce consegue advinhar qual foi? ')
acertou = False
palpites = 0

while not acertou: # enquanto acertou for false o laço continua, o valor de 'acertou' so muda quando a resposta do jogador for == computador tornadno 'acertou' true e finalizando o laço
    jogador = int(input('qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou == True
    else:
        if jogador < computador:
            print('mais.... tente mais uma vez')
        elif jogador > computador:
            print('menos...tente mais uma vez')
print('Acertou com {} tentativas. Parabens!'.format(palpites))