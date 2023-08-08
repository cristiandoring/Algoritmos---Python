#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_digitado = int(input('Digite um número de 0 a 5: '))
#sorteia numero aleatorio
numero_sorteado = random.randint(0,5)

if numero_digitado <0:
    print('Número digitado inválido.') 
elif numero_digitado > 5:
    print('Número digitado inválido.') 
else:
    if numero_digitado == numero_sorteado:
        print('Você venceu!')
    else:
        print('Você perdeu')