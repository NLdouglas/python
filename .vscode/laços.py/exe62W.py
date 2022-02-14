termo = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
primeiro = termo
cont = 1
total = 0
mais = 10 # quantidade de termos q sera mostrado inicialmente
while mais != 0: #laços podem ser aninhados, ou seja, laço dentro de um laço 
    total = total + mais
    while cont <=total:
        print('{} - '.format(primeiro), end='')
        primeiro += razao
        cont +=1
    print('Pausa')
    mais = int(input('quantos termos voce quer mostrar a mais? '))
print('fim')