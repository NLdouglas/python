'''pessoas = {
    'nome': 'gustavo', 'sexo': 'M', 'idade': 22
}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos') #quando for selecionar, usar aspas duplas ou simples se iniciar com dupla
for k, v in pessoas.items():
    print(f'{k} = {v}')  #k = keys,  v = values
del pessoas['sexo'] # deletar um item, chave ou valor
pessoas['nome'] = 'leando' # muda o valor da chave nome
pessoas['peso'] = 98.5 # adiciona chave e valor'''

''''brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)  #adciona os 2 dicionarios a lista, sendo cada dicionario um elemento cada, estado1 = 0, estado2 = 1 

print(brasil)
print(brasil[0] ['uf']) #mostra os elementos do estado1 procurando o valor da chave UF'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')) #cria a chave e faz o valor como input
    estado['sigla'] = str(input('sigla do Estado: '))
    brasil.append(estado.copy()) # faz uma copia dos dicionarios e lagar em lista como elementos separados com k v 
for e in brasil:
    for k, v in estado.items():
        print(f'o campo {k} tem valor {v}')
    for v in estado.values():
        print(v)