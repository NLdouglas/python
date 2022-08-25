'''from functools import partial

def add_numbers(x, y):
    return x + y        #CURRYING = DERIVAR NOVAS FUNÇÕES A PARTIR DE FUNÇÕES EXISTENTES POR MEIO
                            DA APLICAÇÃO PARCIAL DE ARGUMENTOS 

add_five = lambda y:add_numbers(5,y)
print(add_five(add_numbers(5,9)))   mesma coisa que add_five = partial(add_numbers, 5) '''


'''some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)        # EXEMPLO DE ITERADOES

dict_iterador = iter(some_dict)
print(list(dict_iterador))'''



'''def squares(n=10):
    print(f'Gernerating squares from 1 to {n ** 2}')        EXEMPLO DE GERADORES 
    for i in range(1, n + 1):
        yield i ** 2                                              

gen = squares() # so passará a excutar quando começar a solicitar os elementos 

for x in gen:
    print(x, end=' ') #aqui foi solicitado o elemento X assim dando inicio a função '''



'''gen = (x ** 2 for x in range(100))

# mesma coisa que:

def _make_gen():
    for x in range(100):
        yield x **2
gen =  _make_gen()

# usando no lugar de list comprehensions como argumento de função
sum(x ** 2 for x in range(100))

dict((i, i ** 2) for i in range(5))'''