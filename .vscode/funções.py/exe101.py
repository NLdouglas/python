from datetime import datetime

def voto(n=0):
    if n > 16:
        return True
    else:
        return False


pessoa = int(input('Em que ano voce nasceu: '))
res = datetime.now().year - pessoa
if voto(res):
    print(f'Com {res} anos: VOTO OPCIONAL')
else:
    print(f'Com {res} anos: NÃO VOTA')


#SOLUÇÃO CURSO EM VIDEO

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos: VOTO OPCIONAL'
    else:
        return f'com {idade} anos: VOTO OBRIGATORIO.'


nasc = int(input('Em que ano voce nasceu? '))
print(voto(nasc))