def metade(preco, formatar = False):
    metade_preco = preco/2

    #se formatar for falso retorna normal, se for verdadeiro retorna formatado
    return metade_preco if formatar is False else moeda(metade_preco)

def dobro(preco=0,formatar = False):
    dobro_preco = preco * 2

    #se formatar for falso retorna normal, se for verdadeiro retorna formatado
    return dobro_preco if formatar is False else moeda(dobro_preco)

def aumento(preco=0,formatar = False):
    aumento_preco = preco + (preco*0.1)

    #se formatar for falso retorna normal, se for verdadeiro retorna formatado
    return aumento_preco if formatar is False else moeda(aumento_preco)

def desconto(preco=0,formatar = False):
    desconto_preco = preco - (preco*0.1)

    #se formatar for falso retorna normal, se for verdadeiro retorna formatado
    return desconto_preco if formatar is False else moeda(desconto_preco)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')

def resumo(preco):
    print('-'*36)
    print(f'{"RESUMO DO VALOR":^36}')
    print('-'*36)
    print(f'Preço analisado: \t{(moeda(preco))}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'10% de aumento: \t{aumento(preco,True)}')
    print(f'10% de desconto: \t{desconto(preco,True)}')
    print('-'*36)
