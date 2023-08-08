#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço 
#normal e condição de pagamento: – à vista dinheiro/cheque: 10% de desconto – 
#à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal  
#– 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor do produto: '))
print('*** SELECIONE A FORMA DE PAGAMENTO ***')
print('[ 1 ] À vista em dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
forma_pag = int(input(''))

if forma_pag < 1 or forma_pag > 4:
    print('Opção inválida')
else:
    if forma_pag == 1:
        print('Pagamento será à vista em dinheiro/cheque.')
        print('O valor do produto será {:.2f}'.format(valor-(valor*0.1)))
    elif forma_pag == 2:
        print('Pagamento será à vista no cartão.')
        print('O valor do produto será {:.2f}'.format(valor-(valor*0.05)))
    elif forma_pag == 3:
        print('Pagamento será 2x no cartão.')
        print('O valor do produto será {:.2f}'.format(valor))
    else:
        print('Pagamento será à vista 3x ou mais no cartão.')
        print('O valor do produto será {:.2f}'.format(valor+(valor*0.2)))