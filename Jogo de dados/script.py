#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado
import random, time, operator
maior = 0
vencedor = ''
jogadas = {
    'jogada1': random.randint(1,6),
    'jogada2': random.randint(1,6),
    'jogada3': random.randint(1,6),
    'jogada4': random.randint(1,6)
}

ranking = ()
print('=-'*15)
print('VALORES SORTEADOS')
print('=-'*15)
for indice, valor in jogadas.items():
    print(f'{indice} tirou {valor} no dado')
    time.sleep(1)
print('=-'*15)
print('RANKING')

ranking = sorted(jogadas.items(),key=operator.itemgetter(1), reverse=True)
print('=-'*15)
for i,v in enumerate(ranking):
    print(f'{i+1}º - {v[0]}')