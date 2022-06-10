temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] # 1 == PESO 0 == nome
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) # princ faz uma copia de temp sendo duas listas diferente mas com os mesmos valores
    temp.clear() #limpa a lista temp
    resp = str(input('quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'tamanho da lista {len(princ)}')
print(f'o maior peso foi de {mai}kg', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print()
print(f'o menor peso foi de {men}kg', end=' ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
print()