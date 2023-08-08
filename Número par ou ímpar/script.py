#crie um programa que leia um número e mostre se é par ou ímpar
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('{} é par.'.format(numero))
else:
    print('{} é ímpar.'.format(numero))