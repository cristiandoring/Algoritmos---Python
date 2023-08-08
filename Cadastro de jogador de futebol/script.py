#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
#jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No 
#final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

jogador = {}
gols = []
somatorio_gols = 0
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?')
)
for i in range(0,partidas):
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
    somatorio_gols += gols[i]
jogador['gols'] = gols


jogador['total'] = somatorio_gols
print(jogador)

print('=-'*30)

for indice, valor in jogador.items():
    print(f'O campo {indice} tem o valor {valor}.')

print('=-'*30)

print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for indice, valor in enumerate(gols):
    print(f'=> Na partida {indice}, fez {valor} gols.')
print(f'Foi um total de {somatorio_gols} gols.')

