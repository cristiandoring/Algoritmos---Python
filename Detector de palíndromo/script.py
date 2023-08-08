#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. obs(palíndromo são palavras que podem ser lidas igualmente de trás pra frente)

frase = input('Digite uma frase: ')
frase_invertida = frase[::-1]

if frase.replace(' ','') == frase_invertida.replace(' ',''):
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))