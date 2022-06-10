from time import sleep

dados = dict()
partida = list()

dados['jogador'] = str(input('Nome do jogador: '))
jogos = int(input(f'Quantas partidas {dados["jogador"]} jogou: '))
for g in range(0, jogos):
    partida.append(int(input(f' quantos gols na partida {g}? ')))
dados['gols'] = partida[:]
dados['total'] = sum(partida)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')
print('-='*30)
print(f'O jogador {dados["jogador"]} jogous {len(dados["gols"])} partidas')
for i, v in enumerate(dados['gols']):
    print(f'   =>Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')