#Escreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um 
#número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
numero_inteiro = numero_float = 0

def leiaInt(numero_inteiro=0):
    while True:
        try:
            numero_inteiro = int(input('Digite um inteiro: '))
        except:
            print('\033[31mPor favor. Digite um número inteiro válido.\033[m')
        else:
            break
    return numero_inteiro

def leiaFloat(numero_float=0):
    while True:
        try:
            numero_float= float(input('Digite um real: '))
        except:
            print('\033[31mPor favor. Digite um número inteiro válido.\033[m')
        else:
            break
    return numero_float




print(f'O valor inteiro digitado é {leiaInt(numero_inteiro)} e o valor real é {leiaFloat(numero_float)}.')