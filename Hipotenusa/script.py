import math
cateto_adjacente = float(input('Digite a medida do cateto adjacente: '))
cateto_oposto = float(input('Digite a medida do cateto oposto: '))

hipotenusa = math.hypot(cateto_adjacente,cateto_oposto)

print('A hipotenusa do triângulo vale {:.2f}.'.format(hipotenusa))