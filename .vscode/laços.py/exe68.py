from random import randint

while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I] ? ')).upper().strip()[0]
    print(f'voce jogou {jogador} e o computador {computador}. total de {total}')
    if tipo == 'p':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce venceu')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente....')
print(f'game over! voce venceu {v} vezes')