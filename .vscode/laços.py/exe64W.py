# num = 0 
#cont = 0
#soma = 0

num = cont = soma = 0
num = int(input('digite um numero [999 para parar]:'))
while num != 999:
    soma += num # soma todos os numero digitados ( 0 + 1 + 5 +5 ) = soma = 11 
    cont += 1 # soma a quantidade de numeros digitados, usuario digitou 2 numero cont = 2
    num = int(input('digite um numero [999 para parar]:'))
print('voce digitou {} numero e a soma entre eles foi {}'.format(cont, soma)) # cont -1 para n somar o 999, soma -999 para sair o valor correto 