extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove''dez', 'onze', 
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('tente novamente. ', end='')
print(f'voce digitou o numero {extenso[num]}')