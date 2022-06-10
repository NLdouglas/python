lista = list()
for c in range(0, 5):
    n = int(input('digite um valor: '))
    if c == 0 or n > lista[-1]: # se o numero digitado for maior que o anterior então joga para o final da lista
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista): #le a lista do menor ao final da lista
            if n <= lista[pos]: # verifica se N vai ser maior que algum numero da lista é menor ou igual a pos
                lista.insert(pos, n) # se for igual ou menor entao adiciona o numero N na posição POS
                print(f'adicionado na posição {pos} da lista..')
                break
            pos += 1 # passa para a proxima posição 
print(f'os valores digitados em ordem foram {lista}')