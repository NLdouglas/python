time = ('america-MG', 'atlhletico-GO', 'atletico-MG', 'Avai', 'botafogo', 'bragantino', 'internacional', 'gremio', 'flamengo', 'fluminense')
print('os 5 primeiros são ', time[0:5])
print('os 4 ultimos são', time[-4:])
print('Times em ordem alfabetica: ',sorted(time))
print(f'o bragantino esta na {time.index("chapecoense")+1} posição') # +1 pq começa no zero entao apresentara uma posição menor 