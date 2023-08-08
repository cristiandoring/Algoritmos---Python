#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
valor_compra = produto_maior_mil = contador = 0
nome_mais_barato = ''
print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    contador += 1
    print('')
    
    valor_compra += preco

    if preco > 1000:
        produto_maior_mil += 1
    
    
    opcao = input('Quer continuar? [S/N]')

    if contador == 1:
        barato = preco
        nome_mais_barato = produto

    else:
        if preco < barato:
            barato = preco
            nome_mais_barato = produto

    if opcao in 'Nn':
        break
print('------FIM DO PROGRAMA ------')
print(f'Valor total da compra: {valor_compra}.')
print(f'{produto_maior_mil} produto custa mais que R$ 1000,00.')
print(f'O produto mais barato foi {nome_mais_barato} que custou {barato}.')
