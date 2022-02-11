valor1 = int(input('digite um valor: '))
valor2 = int(input('digite outro valor: '))
soma = valor1 + valor2
multiplicar = valor1 * valor2
final = False
while not final:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    resposta = int(input('escolha um numnero acima: '))
    if resposta == 1:
        print(soma)
    if resposta == 2:
         print(multiplicar)
    if resposta == 3:
        if valor1 > valor2:
            print(valor1)
        else: 
            print(valor2)
    if resposta == 4:
        print('escolha os valores novamente!')
        valor1 = int(input('digite um valor: '))
        valor2 = int(input('digite outro valor: '))
    if resposta == 5:
        final == True
    
print('voce finalizou o programa')








