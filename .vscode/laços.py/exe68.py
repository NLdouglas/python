from random import randint
v = 0
while True:
    jogador = int(input('digite um valor? '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' # flag para iniciar outro laço, variavel contem string vazia pois vai receber input com resposta do usuario 
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0] #saida do usuario ira se tornar o valor de tipo
    print(f'Voce jogou {jogador} e o computador {computador}. total {total}', end=' ')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
            if total % 2 == 0:
                print('voce ganhou')
                v += 1
            else:
                print('voce perdeu')
                break
    elif tipo == 'I':
            if tipo % 2 == 1:
                print('voce ganhou')
                v +=1
            else:
                print('voce perdeu')
                break
    print('vamos jogar novamente...')
print(f'Game over! voce venceu {v} vezes')

'''
Primeiro laço serve para inciar sempre o programa com as pergunda de valor
ja o segundo serve para iniciar a resposta do jogador referente a se ele quer PAr ou Impar
dando em seguida a validação dos resultados sendo os IFS para conferir se deu par ou impar
ficar atento as identações dos prints e condições

 '''
