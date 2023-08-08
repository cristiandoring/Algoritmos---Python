#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo 
#usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    print('-'*30)
    numero = int(input('Digite um valor: '))
    print('-'*30)
    
    if numero <0:
        print('Encerrando programa... ')
        break

    for i in range(1,11):
        print(f'{i} x {numero} = {numero*i}')
    