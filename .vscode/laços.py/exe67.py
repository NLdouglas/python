soma = 0
while True:
    n = int(input('qual Numero quer a tabuada: '))
    if n < 0:
        print('programa encerrado')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')