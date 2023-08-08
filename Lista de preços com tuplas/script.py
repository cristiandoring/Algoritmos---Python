#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
#No final, mostre uma listagem de preços, organizando os dados em forma tabular

lista_precos = ('Lápis', 1.75,'Borracha', 2,'Caderno', 15.90,'Estojo', 25,'Trasferidos', 4.20,
                'Compasso', 9.99,'Mochila', 120.32,'Canetas', 22.30,'Livro', 34.90, )

print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)
par = 0
impar = 0
for i in range(0, len(lista_precos)):
    if i % 2 == 0:
        print(f'{lista_precos[i]:.<30}',end='')
    else:
        print(f'R${lista_precos[i]:>7.2f}')
