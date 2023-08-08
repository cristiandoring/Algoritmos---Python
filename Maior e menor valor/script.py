#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre 
#todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele 
#quer ou não continuar a digitar valores

numero = int(input('Digite um número: '))
opcao = input('Quer continuar [S/N]? ')

maior = menor = soma = media = numero
contador_elementos = 1

while True:
    if opcao in ('Ss'):
        numero = int(input('Digite um número: '))
        opcao = input('Quer continuar [S/N]? ')
        contador_elementos += 1
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        soma = soma + numero
        media = soma/contador_elementos
        
    if opcao in ('Nn'):
        print('A quantidade de valores foi {} e a média dos valores digitados foi de {}.'.format(contador_elementos, media))
        print('O maior dos valores digitados foi {}.'.format(maior))
        print('O menor dos valores digitados foi {}.'.format(menor))
        break