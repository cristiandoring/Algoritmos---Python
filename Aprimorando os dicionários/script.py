#Crie um programa que gerencie o aproveitamento de varios jogadores de futebol. O programa vai ler o nome do
#jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No 
#final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
time = []
jogador = {}
gols = []
somatorio_gols = 0

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

    gols.clear()
    for i in range(0,partidas):
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
        somatorio_gols += gols[i]
    jogador['gols'] = gols


    jogador['total'] = somatorio_gols
    time.append(jogador.copy())

    opcao = input('Quer continuar? ') 

    while opcao not in 'NnSs':
        print('ERRO! Responda apenas S ou N.')
        opcao = input('Quer continuar? ')
    if opcao in 'Nn':
        break

print('-'*40)
for i,j in enumerate(time):
    print( f'{i:>3}',end='')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)


