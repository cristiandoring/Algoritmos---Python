#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um 
#dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

galera = []
pessoa = {}
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo [M/F]: ')
   
    while pessoa['sexo'] not in 'MmFf':
        print('ERRO! Responda apenas M ou F.')
        pessoa['sexo'] = input('Sexo [M/F]: ')

    pessoa['idade'] = int(input('Idade: '))    
    
    #soma idades
    soma += pessoa['idade']
    #manda os dados de cada pessoa pra lista galera
    galera.append(pessoa.copy())
    
    opcao = input('Quer continuar? ') 

    while opcao not in 'NnSs':
        print('ERRO! Responda apenas S ou N.')
        opcao = input('Quer continuar? ')

    if opcao in 'Nn':
        break
media = soma / len(galera)

print('-='*30)
print(f'Ao todo tempos {len(galera)} pessoas cadastradas.')
print(f'A média de idades é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ',end='')

for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
    print() 

print('As pessoas com idade acima da média foram ',end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} ',end='')

print("ENCERRANDO")