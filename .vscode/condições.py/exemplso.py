casa = float(input('digite o valor da casa: '))
salario = float(input('seu salario: '))
anos = int(input('prestações: '))
valor = casa / (anos * 12) 
porcentagem = salario * 30 / 100 

print('para pagar uma casa de {:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação sera de R${:.2f}'.format(valor))

if valor <= porcentagem :
    print('emprestimo negado')
else:
    print('emprestimo aceito')
