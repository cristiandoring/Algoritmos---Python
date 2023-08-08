#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

if numero1 > numero2:
    print('O primeiro maior!')
elif numero2 > numero1:
    print('O segundo é maior!'.format(numero2, numero1))
else:
    print('Os números são iguais!'.format(numero1, numero2))