#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
#na ordem de colocação. Depois mostre:
#a) Os 4 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Internacional.

classificacao = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 
                'Athletico PR', 'Fortaleza', 'Cruzeiro', 'Internacional', 'Atlético MG', 'Cuiabá', 'Santos', 
                'Corinthians', 'Bahia', 'Goiás', 'Coritiba', 'Vasco da Gama', 'América MG' )

print('Classificação')
print(classificacao)

print('\nClassificados para a libertadores')
for i in range(0,4):
    print(f'{i+1}º - {classificacao[i]}')

print('\nRebaixados')
for i in range(16,20):
    print(f'{i+1}º - {classificacao[i]}')

print('\n Times em ordem alfabética')
print(sorted(classificacao))

for i in range(0,20):
    if classificacao[i] == 'Internacional':
        posicao = i+1
print(f'\n O Internacional está em {posicao}º colocado')