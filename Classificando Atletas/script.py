#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
#mostre sua categoria, de acordo com a idade: – Até 9 anos: MIRIM – Até 14 anos: INFANTIL 
#– Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER

from datetime import date

nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year
tempo = (ano_atual - nascimento)

if nascimento < 0 or nascimento > ano_atual:
    print('Data de nascimento inválida.')

if tempo >= 0 and tempo <=9:
    print('Categoria mirim.')
elif tempo > 9 and tempo <=14:
    print('Categoria infantil.')
elif tempo > 14 and tempo <=19:
    print('Categoria Junior.')
elif tempo > 19 and tempo <=25:
    print('Categoria Senior.')
else:
    print('Categoria Master.')