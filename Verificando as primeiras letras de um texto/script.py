#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "Santo"

nome_cidade = str(input('Digite o nome de uma cidade: ')).strip()

#imprime verdadeiro ou falso se a frase começa com a palavra 'Santo'
print(nome_cidade.startswith('Santo'))