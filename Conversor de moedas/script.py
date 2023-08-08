dinheiro_real = float(input('Digite o valor: R$ '))

cotacao_atual_dolar = 4.93

dinheiro_dolar = dinheiro_real / cotacao_atual_dolar

print('R$ {:.2f} equivale a U$ {:.2f}.'.format(dinheiro_real,dinheiro_dolar))
