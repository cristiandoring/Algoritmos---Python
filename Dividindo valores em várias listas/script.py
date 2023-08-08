#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras 
#que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

valores = []
lista_pares = []
lista_impares = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    
    #coloca valor na lista par ou ímpar
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)

    opcao = str(input('Quer continuar? [S/N]'))

    while opcao not in 'SsNn':
        print('Opção inválida.')
        opcao = str(input('Quer continuar? [S/N]'))
    if opcao in 'nN':
        break
print(f'Lista original {valores}')
print(f'Lista pares {lista_pares}')
print(f'Lista ímpares {lista_impares}')