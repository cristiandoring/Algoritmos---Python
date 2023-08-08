# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos 
#jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
#composta.
import random
import time
print('-'*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-'*30)
jogos = []
quantidade_jogos = int(input('Quantos jogos você quer jogar? '))

print('-='*5,end=' < ')
print(' GERANDO ', end=' > ')

print('-='*5)
for indice in range(0,quantidade_jogos):
    print(f'Jogo {indice+1}: ', end='')
    jogos = random.sample(range(1, 61), 6)
    jogos.sort()
    print(jogos)
    time.sleep(1)

print('-='*5,end=' < ')
print(' BOA SORTE ', end=' > ')

print('-='*5)