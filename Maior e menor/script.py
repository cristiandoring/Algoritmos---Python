#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Número 1 = '))
n2 = float(input('Número 2 = '))
n3 = float(input('Número 3 = '))

#maior
if n1 > n2 and n1> n3:
    print('Maior = {}.'.format(n1))
elif n2 > n1 and n2> n3:
    print('Maior = {}.'.format(n2))
else:
    print('Maior = {}.'.format(n3))

#menor
if n1 < n2 and n1 < n3:
    print('Menor = {}.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('Menor = {}.'.format(n2))
else:
    print('Menor = {}.'.format(n3))