def metade(preco):
    metade_preco = preco/2

    return metade_preco

def dobro(preco=0):
    dobro_preco = preco * 2

    return dobro_preco

def aumento(preco=0):
    aumento_preco = preco + (preco*0.1)

    return aumento_preco

def desconto(preco=0):
    desconto_preco = preco - (preco*0.1)

    return desconto_preco

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')
