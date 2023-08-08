#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maiores = quantidade_homens = quantidade_mulheres = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [F/M]')
    if idade >18:
        maiores += 1
    if sexo in 'mM':
        quantidade_homens += 1
    if sexo in 'Ff' and idade < 20:
        quantidade_mulheres += 1
    
    print('-'*20)
    
    opcao = input('Quer continuar? [S/N] ')
    if opcao in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {quantidade_homens}')
print(f'Total de mulheres com menos de 20 anos: {quantidade_mulheres}')
