# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo 
#será formado: -EQUILÁTERO: todos os lados iguais; – ISÓSCELES: dois lados iguais, um diferente – 
#ESCALENO: todos os lados diferentes
print('***MEDIDAS DE TRIANGULOS ***\n')

medida1 = float(input('Digite a medida1:'))
medida2 = float(input('Digite a medida2:'))
medida3 = float(input('Digite a medida3:'))

if medida1 < medida2+medida3 and medida2 < medida1+medida3 and medida3 < medida2+medida1:
    print('AS MEDIDAS FORMAM TRIÂNGULOS')
        
    if medida1 == medida2 and medida2 == medida3:
        print('EQUILÁTERO.')
    elif medida1 != medida2 and medida1 != medida3 and medida2 != medida3:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('AS MEDIDAS NÃO FORMAM TRIÂNGULOS')