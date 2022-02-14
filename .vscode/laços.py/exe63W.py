n = int(input('quantos termos voce quer saber: '))
t1 = 0
t2 = 1   # 0 e 1 sao os primeiros termos de fibonacci
print('{} ~~ {}'.format(t1, t2), end='')
cont = 3
while cont <= n: # const ja comeca com o valor 3 devido q a sequencia t1 t2 e t3 sao os mesmos numeros logo o loop n precisa seguir se o valor em n forem iguais ou menores q 3
    t3 =t1 + t2
    print(' ~{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print(' ~fim')
