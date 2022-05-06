def dobra(lst):
    """
    :param lst: lista vazia
    """
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

help(dobra) #docstrings #documentação de uma função criada pelo dev  
    
#parametros opcionais

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(s)

somar(3)'''

#escopo global é quando a variavel foi declarada fora da funcção assim podendo ser utilizada na chamada a função e fora dela

#escolo local variavel é localizada dentro da função entao so pode ser usada na chama a função ou dentro dela

def funcao():
    global n1 # comando para ultilizar a variavel glolbal = a que esta fora da func
    n1= 4 # n1 loca fica com o valor definido na func
    print(f'n1 dentro vale {n1}')

#quando o comando GLOBAL for utilizado a variavel fora da func recebe o valor da var de dentro da func 
n1 = 2 # n1 global tem o valor diferente da func
funcao()
print(f'n1 fora vale {n1}')


#retorno de valor #return

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'os resultados foram {r1} {r2} {r3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('digite um numero: '))
if par(num):
    print('é par')
else:
    print('impar')