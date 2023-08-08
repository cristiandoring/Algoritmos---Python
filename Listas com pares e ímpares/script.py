# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
#que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
# em ordem crescente.


pares = []
impares = []
numeros = [pares,impares]
for indice in range(0,7):
    
    numero = int(input(f'Digite o {indice+1}º elemento: '))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    
#print(numeros)
pares.sort()
impares.sort()
print(f'Os números digitados foram {numeros}')
print(f'A lista dos pares é {pares}')
print(f'A lista dos ímpares é {impares}')