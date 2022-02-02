user = int(input('escolha enre 1 e 10 para saber a tabuada: '))
for n in range(0, 11):
    num = n
    if num <= 10:
        print('{} x {} = {}'.format(n, user, user*n))
