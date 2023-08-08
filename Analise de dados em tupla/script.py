#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
contador_pares = 0
valores = (n1,n2,n3,n4)

print('Você digitou os valores: ', end='')

for i in range(0,4):
    print(valores[i], end=' ')
    if valores[i] % 2 == 0:
        contador_pares +=1
    
print(f'\nO número 9 aparece {valores.count(9)} vezes.')

if 3 in valores:
    print(f'O número 3 está na {valores.index(3)+1}ª posição.')
else:
    print('Não existe o valor 3.')
print(f'A quantidade de valores pares digitados foi de {contador_pares}.')