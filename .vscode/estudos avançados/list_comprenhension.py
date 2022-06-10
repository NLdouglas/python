lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)


#list comprenhension

nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)

"""
Define uma variavel que receber uma nova lista como valor (nova_lista_preco2), dentro da nova lista ela vai receber
o valor definido pelos parametros passados, ou seja, para cada PRECO dentro da lista_precos *2

PRECO * 2 para cada item dentro de lista_preco
"""

imposto2 = [preco * 0.5 for preco in lista_precos if preco > 1000]
print(imposto2)

"""
So vai executar preco * 0.5 se o item dentro de lista_preco for maior que 1000
"""