#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
#No final, mostre os 10 primeiros termos dessa progressão.

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))


for i in range(1,11):
    print(termo1, end=' -> ')  
    termo1 += razao
print('ACABOU')