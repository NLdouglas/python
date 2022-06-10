valores = []
while True:
    num = int(input('digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        print('valor duplicado')
    resp = ' '
    while resp not in  'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()
    if resp == 'N':
        valores.sort()
        print(f'Ecerrado!, os valores digitados foram {valores}')
        break
