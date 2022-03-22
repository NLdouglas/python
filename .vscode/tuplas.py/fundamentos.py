# () = tuplas
lanche =  ('hamburguer', 'suco', 'pizza', 'pudim' )
print(lanche[1:3]) # tratamento de strings com tuplas

for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}') # apresenta os dados mais a posição de cada 

print('comi pra caramba')
print(sorted(lanche)) # mostra a tupla em ordem 

'''
Laço for com 3 formas diferentes dando a mesma saida, enumerade numera todos os valores da tupla
range a mesma coisa 
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c =  b + a #junção das tuplas e nao soma

print(len(c)) #comprimeito

print(c.count(4)) # conta quantas vezes o valor aparece na tupla

print(c.index(2)) #mostra a posição do valor

print(c.index(2, 1)) # primeiro valor mostra qual o programa vai procurar e o segundo apartir da posição desejada, chama - se deslocamento

del(pessoa) #apaga a tupla, apagando da memoria

