#Faça um programa que leia um número qualquer e mostre o seu fatorial. 

numero = int(input('Digite um número: '))
fatorial = 1
i = 1
print('Calculando {}!'.format(numero), end=' ')

while i <= numero:
    print(i,end=' x ')
    fatorial = fatorial * i
    i+=1
print('= {}'.format(fatorial))