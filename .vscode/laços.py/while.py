#tanto FOR quanto  WHILE servem para ser usado quando sabe o limite do laço
#ja quando n se sabe o limite use o WHILE

'''c = 1
while c < 10:
    print(c)
    c += 1 # sem contador de soma o loop fica infinito pq o valro de C n muda e sempre vai continuar contando
print('fim')'''

n =1 
while n != 0: #condição de parada se o numero for 0 
    n = int(input('digite um valor: '))
print('fim') # laço continua ate o usuario digitar 0

r = 'S'
while r == 'S':
    n = int(input('digite um valor: '))
    r = str(input('quer continuar? [S/N]')).upper() # enquanto usuario digitar S o loop continua
print('fim')

n = 1
par = impar = 0 #duas variaveis com o valor 0 
while n != 0: #condição de parada
    n = int(input('digite um valor: '))
    if n != 0: # se o numero for diferete de 0 segue com o laço se não aciona a condição de parada interrompendo o laço
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('voce digitou {} numeros pares e {} numeros impares'.format(par, impar))