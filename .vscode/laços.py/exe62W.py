termo = int(input('digite o termo: '))
razao = int(input('digite a razao: '))
primeiro = termo
cont = 0
while cont <=10:
    print('{} - '.format(primeiro), end='')
    primeiro += razao
    cont +=1
print('fim')