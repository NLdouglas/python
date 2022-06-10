frase = (input('digite uma frase: ')).strip() # tira os espaços
palavra = frase.split() #separa por cada palavras gerando uma lista
junto = ''.join(palavra) # junta todas as palavras sem espaços
inverso = '' # string vazia pois vai recever palavras ao contrario
inverso = junto[::-1] # do inicio ao fim de tras para frente
for letra in range(len(junto)-1, -1, -1):                            #ordem do -1  #-1 pois começa do 0 ao ultimo entao precisa do menos -1 para contar a ultima letra
    inverso += junto[letra]  #cada palavra em JUNTO passa pelo laço                #-1 começa da ultima letra 
print('o inverso de {} é {}'.format(frase, inverso))
if inverso == junto:        #LETRA lendo de tras para frente jogando              # -1 continuar a contagem de tras para frente, sendo da ultima, penultima, etc.. 
    print('temos um palindromo')#cada letra dentro da variavel INVERSO
else:
    print('nao temos um palindromo')