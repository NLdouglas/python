termo = int(input('digite o termo da PA: '))
razao = int(input('razao: '))
decimo = termo + (10) * razao # primeiro numero, repetindo 10x pulando * o numero da razao
for c in range(termo, decimo, razao):
    print('{}'.format(c))
print('acabou')