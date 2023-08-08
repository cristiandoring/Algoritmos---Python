# Adapte o exercicio de exercitando módulos, criando uma função adicional chamada moeda() que consiga mostrar os
#números como um valor monetário formatado.

import moeda


preco = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro do {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos R$ {moeda.moeda(moeda.aumento(preco))}')
print(f'Descontando 10%, temos R$ {moeda.moeda(moeda.desconto(preco))}')