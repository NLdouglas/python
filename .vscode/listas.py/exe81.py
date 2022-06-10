lista = list()
cont = 0
while True:
    valor = int(input('digite um valor: '))
    cont += 1
    lista.append(valor)
    lista.sort(reverse=True)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'voce digitou {cont} elementos')
print(f'Os valores em ordem dec são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('n tem o valor 5 na lista')



# RESP CURSO EM VIDEO

valores = []
while True:
    valores.append(int(input('digite um numero: ')))
    resp = str(input('quer continuar [s/n]'))
    if resp in 'Nn':
        break
    print(f'voce digitou {len(valores)} elementos')
    #restante segue igual ao primeiro 