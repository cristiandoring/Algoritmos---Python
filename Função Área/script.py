# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
#(largura e comprimento) e mostre a área do terreno.

def area(largura,comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.2f}m x {comprimento:.2f}m é de {area:.2f}m².')

print(f'{"Controle de Terrenos":^30}')
print('-'*30)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura,comprimento)