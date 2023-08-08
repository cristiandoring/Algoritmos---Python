#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anos = int(input('Digite em quantos anos você irá pagar: '))

valor_mensalidade = valor_casa/(12*anos)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(valor_casa, anos, valor_mensalidade))
if valor_mensalidade > 0.3*salario:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')

