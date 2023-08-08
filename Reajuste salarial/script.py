salario = float(input('Digite o salário do funcionário: R$ '))
aumento = float(input('Digite o percentual do aumento: '))

salario_atual = salario + salario*(aumento/100)

print('O funcionário que ganhava R$ {:.2f}, com {:.2f}% de aumento, passa a receber R$ {:.2f}.'.format(salario, aumento, salario_atual))