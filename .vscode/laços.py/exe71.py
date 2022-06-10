print('{:^30}'.format('Banco CEV'))
valor = int(input('Que valor Voce quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('volte sempre ao BANCO CEV! tenha um bom dia')

'''
deixa o valor da cedula pré determinado assim quando o usuario digitar o valor total
o programa executa o laço diminuindo o valor total pelo valor da cedula pré definida ao maximo
que der sem exceder o valor da cedula proposta, assim iniciando as condições onde pegara o valor total
e vai diminuir ate o maximo de cada cedula e ira interromper o laço chegando a 0 e exibindo a quantidade
de cada cedula que foi usada pra retitrar o dinheiro
'''

'''
MELHORAR O CODIGO

ACRESCENTAR CENTAVOS ASSIM DEIXAR O INT COMO FLOAT
ADICIONAR UMA CONDIÇÃO EM CASO DO USUARIO DIGITAR ALGO DIFERENTE DE NUMERO

'''