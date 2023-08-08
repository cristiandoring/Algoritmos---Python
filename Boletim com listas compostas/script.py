# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas 
#de cada aluno individualmente.

individuo = []
media = 0

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    media = (nota1 + nota2)/2

    #adiciona cada valor lido em uma lista
    individuo.append([nome, [nota1,nota2],media])

    #laço para continuar
    opcao = input('Quer continuar? [S/N]')

    while opcao not in 'SsNn':
        opcao = input('Quer continuar? [S/N]')
    
    if opcao in 'Nn':
        break

   

print('-'*30)
print('{:^30}'.format('MÉDIAS'))
print('-'*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)

for i, aluno in enumerate(individuo):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-'*30)
    opcao_nota = int(input('Mostrar nota de qual aluno: '))

    while opcao_nota <0 or opcao_nota > len(individuo):
        opcao_nota = int(input('Aluno inexistente. Mostrar nota de qual aluno: '))

    
    if opcao_nota == 999:
        break

    if opcao_nota <= len(individuo):
        print(f'Notas de {individuo[opcao_nota-1][0]} são {individuo[opcao_nota-1][1]}.')