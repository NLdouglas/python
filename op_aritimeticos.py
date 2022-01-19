n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2 #soma
m = n1 * n2  #mult
d = n1 / n2  #divisão
di = n1 // n2  #divisão inteira
e = n1 ** n2  #potencia

print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end='' )  # end =  e no final não faça nada (sem quebra de liunha)
print('Divisão inteira {} e potência {}'.format(di, e))
