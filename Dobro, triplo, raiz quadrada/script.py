import math
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3

#raíz quadrada
#raiz_quadrada = numero ** (1/2)
raiz_quadrada = math.sqrt(numero)

print('O dobro de {} é {}'.format(numero, dobro))
print('O triplo de {} é {}'.format(numero, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(numero, raiz_quadrada))

