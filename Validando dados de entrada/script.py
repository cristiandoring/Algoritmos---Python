#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do 
#Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(numero):
    if numero.isnumeric():
        print(f'Você digitou o número {numero}.')
    else:
        print('Erro! Digite um número inteiro válido.')

numero = input('Digite um número: ')
leiaInt(numero)