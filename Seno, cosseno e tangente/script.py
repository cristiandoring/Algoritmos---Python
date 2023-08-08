import math

angulo = float(input('Digite o valor de um ângulo: '))

#converte para radiano e calcula
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo digitado foi: {:.2f}º'.format(angulo))
print('O Seno de {:.2f}º é {:.2f}.'.format(angulo,seno))
print('O Cosseno de {:.2f}º é {:.2f}.'.format(angulo,cosseno))
print('A Tangente de {:.2f}º é {:.2f}.'.format(angulo,tangente))
