altura = float(input('Digite a medida da altura da parede: '))
largura = float(input('Digite a medida da largura da parede: '))
metros_quadrados_por_litro = float(input('Digite quantos metros quadrados a tinta pinta por litro: '))

quantidade_tinta = (altura * largura) / metros_quadrados_por_litro

print('É necessário {:.4f}l de tinta para pintar uma parede {:.2f}X{:.2f}'.format(quantidade_tinta,altura,largura))