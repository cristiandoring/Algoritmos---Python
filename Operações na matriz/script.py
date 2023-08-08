#Aprimore o desafio anterior, mostrando no final:                                                    
#A) A soma de todos os valores pares digitados.                                                
#B) A soma dos valores da terceira coluna.                                                                                                                
#C) O maior valor da segunda linha.

valores = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]
soma_pares = soma_terc_col = maior = 0

for i in range(0,3):
    for j in range(0,3):
        valores[i][j] = int(input(f'Digite o valor [{i},{j}] = '))

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{valores[linha][coluna] :^8}]',end=' ')
        if valores[linha][coluna] % 2 == 0:
            soma_pares += valores[linha][coluna]
        if coluna == 2:
            soma_terc_col += valores[linha][2]
        if linha == 1:
            if coluna == 0:
                maior = valores[1][0]
            else:
                if valores[1][coluna] > maior:
                    maior = valores[1][coluna]

        
    print()

print(f'A soma dos números pares é {soma_pares}.')
print(f'A soma dos elementos da terceira coluna é {soma_terc_col}.')
print(f'O maior elemento da segunda linha é {maior}.')