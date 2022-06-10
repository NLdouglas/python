from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Nº carteira de trabalho.(Digite 0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = (dados['idade'] + dados['contratação']) - datetime.now().year + 35
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
    