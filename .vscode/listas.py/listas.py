'''num = [2, 3, 9, 1]
num[2] = 3 # troca os valores da lista 
num.append(7) # insere no final da lista o valor desejado
num.sort(reverse=True) #coloca em ordem numerica do menor ao maior, reverse(true) coloca em ordem decrescente
num.insert(2, 0) # insere o numero 2 na posição 0, inicia com o numero e apos a posição
num.pop() #elimina o elemento final, se for colocado numero dentro do () indica a posição e n o valor inserido
num.remove() #pega do inicio da lista eliminadno o primeiro valor existente 
if 5 in num:
    num.remove(5) #faz a verificação na lista toda
else:
    print('nao existe o numero 5')'''

'''valores = list()
valores.append(9)
valores.append(0)
valores.append(7)

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
b = a #ligando uma lista na outra, ou seja, ambas viram a mesma
b = a[:] #faz uma copia da lista desejada, ambas diferentes porem com os mesmos elementos
b[2] = 8
print(f'lista A:{a}')
print(f'lsita B:{b}')'''

from re import X


t = []
t.append(['x'])
print(t)
