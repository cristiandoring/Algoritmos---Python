#Faça um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da 
#progressão usando a estrutura while

print('Gerador de PA')
print('-='*10)

contador = 0

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = termo1
print(termo1, end=' -> ')

while contador < 9:
    termo = termo+razao
    print(termo,end=' -> ' )
    contador += 1
print('FIM')