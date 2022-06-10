import enum


ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 1: '))
    media = (nota1 + nota2) / 2 
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *35)
    opc = int(input('Mostrar mais notas de qual aluno? (999 interromeper): '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'notas de {ficha[opc] [0]} são  {ficha[opc] [1]}') # 0 pega a lista com o nome e 1 pega a lista com as notas
print('volte sempre')