preco = 1000 

def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(preco))


calcular_imposto2 = lambda x: x * 0.3 #primeiro X seria o valor e o segundo o X parametro

print(calcular_imposto2(preco))


#APLICANDO LAMBDA DENTRO DE METODOS

precos = [100, 500, 10, 25]

impostos = list(map(lambda x: x*0.3, precos))
#primeiro X = equivale a variavel precos tornando ela um parametro
#segundo X = equivale a cada valor dentro da lista *0.3
#precos = define a variavel que a funcao lambda deve usar como parametro 