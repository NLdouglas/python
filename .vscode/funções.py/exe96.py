def area(larg, comp):
    a = larg * comp
    print(f'a area de um terreno {larg}x{comp} é de {a}m².')


l = float(input('largura: '))
c = float(input('comprimento: '))
area(l, c)