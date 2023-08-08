#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
numeros = [1, 2, 3]


jogada_cpu = random.choice(numeros)

print('*** PEDRA, PAPEL E TESOURA ***')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')

jogada_player1 = int(input('Digite a jogada: '))
print('\n')


#substitui jogada da cpu número pelo nome da jogada
if jogada_cpu == 1:
    jogada_cpu_txt = 'Pedra'
elif jogada_cpu == 2:
    jogada_cpu_txt = 'Papel'
else:
    jogada_cpu_txt = 'Tesoura'

#substitui jogada do player número pelo nome da jogada
if jogada_player1 == 1:
    jogada_player1_txt = 'Pedra'
elif jogada_player1 == 2:
    jogada_player1_txt = 'Papel'
else:
    jogada_player1_txt = 'Tesoura'

if jogada_player1 <1 or jogada_player1 > 3:
    print('Jogada inválida.')
else:
    print('Pedra')
    sleep(1)
    print('Papel')
    sleep(1)
    print('Tesoura')
    sleep(1)
    print('='*25)
    print('Jogada CPU = {}.'.format(jogada_cpu_txt))
    print('Jogada Player = {}.'.format(jogada_player1_txt))
    print('='*25)
    print('\n')
    if jogada_player1 == jogada_cpu:
        print('EMPATE')
    elif jogada_player1 == 1 and jogada_cpu == 2:
        print('CPU venceu')
    elif jogada_player1 == 1 and jogada_cpu == 3:
        print('Player venceu')
    elif jogada_player1 == 2 and jogada_cpu == 1:
        print('Player venceu')
    elif jogada_player1 == 2 and jogada_cpu == 3:
        print('CPU venceu')
    elif jogada_player1 == 3 and jogada_cpu == 1:
        print('CPU venceu')
    else:
        print('Player venceu')