lista1 = list()
listaP = list()
listaI = list()

while True:
    num = (int(input('digite um valor: ')))
    lista1.append(num)
    resp = str(input('Quer continuar: [S/N] ')).upper()
    if resp == 'N':
        break
print(lista1)
for num in lista1:
    if num % 2 == 0:
        listaP.append(num)
    else:
        listaI.append(num)
print(listaP)
print(listaI)