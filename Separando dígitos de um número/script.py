#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = str(input('Digite um número de 0 a 9999: '))

#preenche 4 casas vazias, no máximo, com zero a esquerda
numero_formatado = numero.zfill(4)
print('Unidade: {}'.format(numero_formatado[3]))
print('Dezena: {}'.format(numero_formatado[2]))
print('Centena: {}'.format(numero_formatado[1]))
print('Milhar: {}'.format(numero_formatado[0]))