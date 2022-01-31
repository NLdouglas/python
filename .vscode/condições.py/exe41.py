from doctest import master


ano = int(input('digite o ano em que nasceu: '))
data = 2022 - ano
print('sua idade é {}'.format(data))
if data <= 9:
    print('mirin')
elif data <=14:
    print('infantil')
elif data <= 19:
    print('junior')
elif data <= 20:
    print('senior')

else:
    print('master')