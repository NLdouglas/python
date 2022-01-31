from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('qual a sua jogada: '))
print('Computador jogou {}'.format(itens[computador])) #colocando a variavel computador entre [] passa a ler os itens como numeros
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('jogada invalida')
elif computador == 1: #computador jogou papel
    if jogador == 1:
        print('empate')
    elif jogador == 0:
        print('computador venceu')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('jogada invalida')
elif computador == 2: #jogou tesoura
    if jogador == 2:
        print('empate')
    elif jogador == 0:
        print('jogador venceu')
    elif jogador == 1:
        print('computador venceu')
    else:
        print('jogada invalida')
