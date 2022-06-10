def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;mErro! Digi te um numero valido.\033[m')
        if ok: # para a contiunuação do laço
            break
    return valor
    
n = leiaint('digite um numero: ')
print(f'voce acabou de digitar um numero {n}')