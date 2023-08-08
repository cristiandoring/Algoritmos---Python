#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um 
#dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

pessoa ={}

pessoa['nome'] = input('Nome: ')
idade = datetime.datetime.today().year - int(input('Ano de nascimento: ')) 
pessoa['idade'] = idade
pessoa['ctps']= int(input('Carteira de trabalho (0 se não tem): '))

#só le se tiver carteira de trabalho
if pessoa['ctps'] <0:
    print('Valor inválido.')
elif pessoa['ctps'] == 0:
    print()
else:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (pessoa['ano_contratacao'] + 35) - datetime.datetime.today().year

print('-='*30)
aposentadoria = 35+pessoa['idade']
for indice, valores in pessoa.items():
    print(f'- {indice} tem o valor {valores}.')
