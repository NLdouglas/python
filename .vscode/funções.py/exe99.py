from time import sleep


def maior(*valores):
    sleep(2)
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{valores} foram informados {len(valores)} valores ao todo.')
    print(f'o maior valor passado foi {max(valores)}')
    print('='*30)
    sleep(1.5)

maior(2, 5 ,9)        
maior(9, 5, 15)
maior(5, 6, 55, 20, 48, 45)