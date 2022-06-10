termo = int(input('digite o termo da PA: '))
razao = int(input('digite a razao da PA: '))
primeiro = termo
cont = 1
while cont <= 10:
    print(primeiro, end=' - ')
    primeiro += razao
    cont +=1
print('fim')

