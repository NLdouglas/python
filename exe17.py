import math
import math
oposto = float(input('digite o cateto oposto: '))
adjacente = float(input('digite o cateto adjacente: '))
hipot = math.hypot(oposto, adjacente)
print('a hipotenusa vai medir {:.2f}'.format(hipot))
