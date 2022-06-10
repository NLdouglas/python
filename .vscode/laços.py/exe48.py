soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1 # cont +=1 
        soma = soma + n # soma += c 
print(soma)
print(cont)