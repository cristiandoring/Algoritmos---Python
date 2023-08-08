#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
#pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
contador_maiores=0
contador_menores=0
ano_atual = date.today().year

for i in range(1,8):
    ano_nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(i)))    
    if ano_atual - ano_nasc >= 18:
        contador_maiores += 1
    else: 
        contador_menores += 1

print('Das pessoas informadas, {} são maiores de idade e {} são menores.'.format(contador_maiores, contador_menores))
