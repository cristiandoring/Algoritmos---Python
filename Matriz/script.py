#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

valores = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]

for i in range(0,3):
    for j in range(0,3):
        valores[i][j] = int(input(f'Digite o valor [{i},{j}] = '))

for linha in valores:
    for elemento in linha:
        print(f'[{elemento :^8}]',end=' ')
    print()