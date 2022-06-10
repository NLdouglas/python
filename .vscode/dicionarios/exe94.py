galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear() # apos a ultima pergunta salva o dict em uma lista e limpa a resps fazendo um dict vazio
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro!! por favor, digite somente F ou M.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('Erro!! Responda apenas com S ou N')
    if resp == 'N':
        break
print('-='*30)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')