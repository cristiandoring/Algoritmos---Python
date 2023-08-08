#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
#mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

numeros = list()

def sorteia(numeros):
    
    print(f'Sorteando 5 valores: ',end='')
    
    for i in range(0,5):
        numeros.append(randint(1,9))
        print(numeros[i], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')
    
def somaPares(numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}.')

sorteia(numeros)
somaPares(numeros)