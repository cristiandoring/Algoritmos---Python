 #Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

contador = 0
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))   

while contador != 5:
    
    print('\n')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('\n')

    opcao = int(input('Digite sua opção: '))
    

    if opcao < 0 or opcao > 5:
        print('Opcão inválida.')
    else:
        if opcao == 1:
            print('A soma entre {} e {} é {}.'.format(numero1, numero2, (numero1 + numero2))) 
        elif opcao == 2:
            print('A multiplicacao entre {} e {} é {}.'.format(numero1, numero2, (numero1 * numero2))) 
        elif opcao == 3:
            if numero1 > numero2:
                print('Entre {} e {} o maior é {}.'.format(numero1, numero2, numero1))
            elif numero2 > numero1:
                print('Entre {} e {} o maior é {}.'.format(numero1, numero2, numero2))
            else:
                print('Os números são iguais.')
        elif opcao == 4:
            numero1 = int(input('Digite o primeiro número: '))
            numero2 = int(input('Digite o segundo número: '))   
        else:
            print('Você escolheu encerrar o programa.')
            contador = 5
