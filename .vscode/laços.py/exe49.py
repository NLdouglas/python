num = int(input('escolha enre 1 e 10 para saber a tabuada: '))
for n in range(1, 11):
    print('{} x {:2} = {}'.format(num, n, num*n))
    