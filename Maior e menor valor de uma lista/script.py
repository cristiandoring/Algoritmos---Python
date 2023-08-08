#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = 0
for contador in range(0,5):
    valores.append(int(input(f'Digite o {contador+1}º elemento: ')))
posicao_maiores = []

print('-'*30)
print('Lista de valores')
print(valores)
print('-'*30)
menor = valores[0]

for posicao in range(0,5):
    if valores[posicao] > maior:
        maior = valores[posicao]
        posicao_maior = posicao
    if valores[posicao] < menor:
        menor = valores[posicao]
        posicao_menor = posicao

print(f'O maior elemento é {maior} e esta nas posições ', end='')

#percorre cada posicao da lista pra ver quantas vezes e quais posicoes o maior aparece
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O maior elemento é {menor} e esta nas posições ', end='')

#percorre cada posicao da lista pra ver quantas vezes e quais posicoes o menor aparece
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()