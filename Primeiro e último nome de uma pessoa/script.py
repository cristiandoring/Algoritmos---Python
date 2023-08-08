#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
#último nome separadamente.

nome = str(input('Digite seu nome: ')).strip().upper()

#imprime do inicio até encontrar espaço pela primeira vez
print('O nome é {}.'.format(nome[0:nome.find(' ')]))

print('O sobrenome é {}.'.format(nome[nome.rfind(' '):]))

