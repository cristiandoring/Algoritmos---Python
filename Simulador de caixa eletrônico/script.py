#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário 
#qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor 
#serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*20)
print('{:^20}'.format('CAIXA ELETRÔNICO'))
print('='*20)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
nota = 50
quantidade_notas = 0
while True:
    if total >= nota:
        total -= nota
        quantidade_notas +=1
    else:
        if quantidade_notas > 0:
            print(f'Total de {quantidade_notas} notas de R$ {nota}.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        quantidade_notas = 0
        if total == 0:
            break
print('Volte sempre!')
print('---FIM DO PROGRAMA---')
