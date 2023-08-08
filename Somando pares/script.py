#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for i in range(1,7):
    numero = int(input('Digite o número{}: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        contador +=1
print('Você informou {} números pares e a soma entre eles é {}.'.format(contador,soma))
