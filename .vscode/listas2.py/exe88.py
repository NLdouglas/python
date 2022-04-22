from random import randint
from time import sleep
lista = list()
jogos = list()

quant = int(input('Quantos jogos voce quer sortear? '))
tot = 1 # valor para iniciar o laçoe n dar erro

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1 # contador para n ultrapassar de 6 numeros em cada lista 
        if cont >= 6: # assim que é sorteado 6 numeros ele para o laço
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1.5)

