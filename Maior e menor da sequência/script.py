#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(i)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(maior, menor))
