from time import sleep



def contador(i, f, p):
    print(f'contagem de {i} ate {f} de {p} em {p}')
    sleep(1)
    if i < f:
        cont = i 
        while cont <= f:
            print(f'{cont} ', end='' )
            sleep(0.5)
            cont += p 
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0 ,2)
print('agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('fim:  '))
pas = int(input('Passo: '))
contador(ini, fim, pas)