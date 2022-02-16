termo = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
primeiro = termo
cont = 1
mais = 10 # quantidade de termos iniciais 
total = 0
while mais != 0:
    total = total + mais # total passou a receber o valor de mais ou seja vai mostrar os 10 primeiros termos
    while cont <= total: #numero de termos 
        print(primeiro, end=' - ')
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('quantos termos voce que mostrar a mais: '))
print('fim')
        