import math
angulo = int(input('digite um angulo qualquer: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('o seno de {} é {:.2f}, coseno {:.2f} e a tangente é {:.2f} \n'
.format(angulo, seno, coseno, tan))