dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Nota'] = float(input(f'Media de {dados["Nome"]}: '))
print(f'- O nome é igual a {dados["Nome"]}')
print(f'- média é igual a {dados["Nota"]}')
if dados['Nota'] >= 7:
    print('- Situação é igual a Aprovado')
else:
    print('- Situação é igual a Recuperação')

# SOLUÇÃO CURSO EM VIDEO

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
