ano = int(input('digite o ano em que nasceu: '))
data = 2022 - ano
idade = data - 18

if data == 18:
    print('está na hora de se alistar')
elif data > 18:
    print('já passou do tempo do alistamento, faz {} anos que deveria'.format(idade))
else:
    print('não tem a idade minima para o alistamento, faltam {}anos'.format(idade))
    
    #o calculo da idade pode ser feito no (format.(data - 18))