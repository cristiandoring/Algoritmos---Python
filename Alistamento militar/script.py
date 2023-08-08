#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele 
#ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do 
#alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#capturar ano atual
from datetime import date

ano_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year

tempo = ano_atual - ano_nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, tempo, ano_atual))
if tempo > 18:
    print('Já passou o tempo de se alistar.')
elif tempo < 18:
    print('Você ainda precisa se alistar quando completar 18 anos.')
else:
    print('Você precisa se alistar esse ano.')