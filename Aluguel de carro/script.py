distancia = (float(input('Digite a distância percorrida em km: ')))
dias = int(input('Digite a quantidade de dias:'))

preco = (60 * dias) + (0.15 * distancia)

print('O preço do aluguel foi R$ {:.2f}'.format(preco))

