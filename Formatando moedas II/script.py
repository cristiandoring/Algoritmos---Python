# Modifique as funções que foram criadas no desafio formatando moedas  para que elas aceitem um parâmetro 
#a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()

import moeda


preco = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(preco)} é {(moeda.metade(preco,True))}')
print(f'O dobro do {moeda.moeda(preco)} é {(moeda.dobro(preco,True))}')
print(f'Aumentando 10%, temos R$ {(moeda.aumento(preco,True))}')
print(f'Descontando 10%, temos R$ {(moeda.desconto(preco,True))}')