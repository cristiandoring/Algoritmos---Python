#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e 
#o maior valor que estão na tupla.
import random

valores=(random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9), random.randint(0,9))

print(f'Os valores sorteados foram {valores}')
print(f'Maior elemento é {max(valores)}')
print(f'Menor elemento é {min(valores)}')