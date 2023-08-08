import moeda

def resumo(preco):
    print('-'*36)
    print(f'{"RESUMO DO VALOR":^36}')
    print('-'*36)
    print(f'Preço analisado: \t{(moeda.moeda(preco))}')
    print(f'Dobro do preço: \t{moeda.dobro(preco,True)}')
    print(f'Metade do preço: \t{moeda.metade(preco,True)}')
    print(f'10% de aumento: \t{moeda.aumento(preco,True)}')
    print(f'10% de desconto: \t{moeda.desconto(preco,True)}')
    print('-'*36)


