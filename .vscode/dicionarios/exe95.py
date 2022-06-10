time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Qauntas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  quantos gols na partida{c} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S OU N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
        print(f'{k:>3}', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()
print('-'* 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'erro! não existe jogador com codigo{busca}!')
    else:
        print(f'-- levantamento do jogador {time[busca] ["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gols.')
    print('-='*30)