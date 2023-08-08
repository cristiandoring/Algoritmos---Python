# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um
#programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input('Digite um preço: R$ '))

moeda.metade(preco)
moeda.dobro(preco)
moeda.aumento(preco)
moeda.desconto(preco)

