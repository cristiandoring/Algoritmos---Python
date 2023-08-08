preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite o percentual de desconto: '))

preco_descontado = preco - preco*(desconto/100)

print('O produto que custava R${:.2f} custará R$ {:.2f} após o desconto de {:.1f}%.'.format(preco, preco_descontado,desconto))