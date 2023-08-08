#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
#podem ou não formar um triângulo.

medida1 = float(input('Digite a medida 1: '))
medida2 = float(input('Digite a medida 2: '))
medida3 = float(input('Digite a medida 3: '))

if medida1 < medida2 + medida3 and medida2 < medida1 + medida3 and medida3 < medida1 + medida2:
    print('As medidas possibilitam formar um triângulo.')
else:
    print('Impossível formar um triângulos com essas medidas.')
 