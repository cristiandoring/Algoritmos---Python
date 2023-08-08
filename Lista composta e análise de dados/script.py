#Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.                                                                                                                
#B) Uma listagem com as pessoas mais pesadas.                             
#C) Uma listagem com as pessoas mais leves.

conjunto_pessoas=[]
pessoas = []

mais_pesado = menos_pesado = 0

while True:
    pessoas.append(input('Nome: '))
    pessoas.append(float(input('Peso: ')))
    
    if len(conjunto_pessoas) == 0:
        mais_pesado = menos_pesado = pessoas[1]
    else:
        if pessoas[1] > mais_pesado:
            mais_pesado = pessoas[1]
        if pessoas[1] < menos_pesado:
            menos_pesado = pessoas[1]
    #junta os dados em uma lista só
    conjunto_pessoas.append(pessoas[:])
    
    #apaga os dados temporários que acabaram de ser armazenados e foram salvos na lista geral
    pessoas.clear()

    opcao = input('Quer continuar? [S/N]')

    while opcao not in 'SsNn':
        opcao = input('Quer continuar? [S/N]')
    
    if opcao in 'Nn':
        break
    
#print(f'A quantidade de pessoas cadastrada foi de {len(pessoas)}.')

print(f'A quantidade de pessoas cadastradas foi de {len(conjunto_pessoas)}.')
print(f'O maior peso foi de {mais_pesado}Kg. Peso de', end=' ')
for pessoa in conjunto_pessoas:
    if pessoa[1] == mais_pesado:
        print(f'{pessoa[0]}',end=' ')

print()
print(f'O menor peso foi de {menos_pesado}Kg. Peso de', end=' ')
for pessoa in conjunto_pessoas:
    if pessoa[1] == menos_pesado:
        print(f'{pessoa[0]}', end=' ')