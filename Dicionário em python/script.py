#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.

alunos = {}

alunos['nome'] = input('Nome: ')
alunos['media'] = float(input('Média: '))

print(f'{alunos["nome"]} ficou com média de {alunos["media"]}.')
if alunos['media'] >= 7:
    print('APROVADO')
elif alunos['media'] > 5 and alunos['media'] <7:
    print('EM RECUPERAÇÃO')
else:
    print('REPROVADO')
