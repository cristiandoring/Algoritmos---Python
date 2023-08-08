#salva o texto digitado ignorando espaços inúteis
nome = str(input('Digite seu nome: ')).strip()

nome_sem_espaco = nome.replace(' ','')

#a variável recebe a posição que tem o espaço vazio - como inicia 
# m zero, será igual ao tamanho do primeiro nome
quantidade_letras_primeiro_nome = nome.find(' ')
print('Seu nome em maíusculas fica: {}.'.format(nome.upper()))
print('Seu nome em minúsculas fica: {}.'.format(nome.lower()))

#conta a quantidade de letras excluindo os espaços entre as palavras
print('O nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {}.'.format(quantidade_letras_primeiro_nome))


