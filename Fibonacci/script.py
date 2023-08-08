#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma 
#Sequência de Fibonacci.

numero = int(input('Digite um valor: '))
i = 0
termo1 = 0
termo2 = 1
termo = 0

if numero == 0:
    print('Não foi solicitado nenhum termo.')
else:
    print(termo1, end=' - ')
    print(termo2, end=' - ')
    while i < numero-2:
        termo = termo1+termo2
        termo1 = termo2
        termo2 = termo
        print(termo, end=' - ')
        i+= 1
    print('FIM')