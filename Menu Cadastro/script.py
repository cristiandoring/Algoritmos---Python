#Faça um programa que cadastre o nome e a idade de pessoas em um arquivo

from menu import menu
from arquivo import *



arq = 'dados.txt'

#verificar se arquivo existe
if arquivoExiste(arq):
    print('Arquivo encontrado.')

#se não existe ele cria um
else:
    criarArquivo(arq)

#le a opção
while True:
    menu()
    #testes de erros possíveis
    try:
        opcao = int(input('\033[32mSua opção: \033[0m'))
        if opcao not in (1, 2, 3):
            raise ValueError
    except (ValueError, TypeError):
        print('\033[31mPor favor. Digite um número inteiro válido.\033[m')
        
    else:
        #ENCERRA PROGRAMA
        if opcao == 3:
            print('-'*30)
            print(f'{"ENCERRANDO PROGRAMA":^30}')
            print(f'{"VOLTE SEMPRE!":^30}')
            break     
        #MOSTRA USUÁRIOS
        elif opcao == 1:
            print('-'*30)
            print(f'{"USUÁRIOS CADASTRADOS":^30}')
            print('-'*30)
            lerArquivo(arq)
        #CADASTRA USUÁRIOS
        elif opcao == 2:
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            
            cadastrar(arq,nome,idade)
