try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario prefiriu nao informar os dados!')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('volte sempre! muito obrigado!')