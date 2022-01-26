from posixpath import split


num = input('digite um numero: ')
print('unidade {} \n dezena {} \n centena {} \n milhar {}'.format(num[:0], num[1], num[2], num[3]))

#erro se n colcoar os 4 digitos
