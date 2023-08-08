#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador 
#perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
contador = 0

print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

while True:
    numero_sorteado_cpu = random.randint(0,10)
    print('-'*30)
    numero = int(input('Diga um valor: '))
    opcao = input('Par ou ímpar [P/Í]? ')
    
    if opcao in 'pP':
        opcao_cpu = 'I'
    elif opcao in 'Ii':
        opcao_cpu = 'P'
    else:
        print('Opção inválida.')
        print('Finalizando programa...')
        break

    print('-'*30)
    if (numero_sorteado_cpu + numero )% 2 == 0:
        resultado = 'par'  
        print(f'Você jogou {numero} e o computador jogou {numero_sorteado_cpu}. Total deu {numero + numero_sorteado_cpu} que é par')
    else:
        resultado = 'impar'
        print(f'Você jogou {numero} e o computador jogou {numero_sorteado_cpu}. Total deu {numero + numero_sorteado_cpu} que é ímpar')
    print('-'*30)

    #possibilades de vitoria maquina
    if resultado == 'par' and opcao_cpu in 'Pp':
        print('Você perdeu!')
        print('GAME OVER')
        print(f'Você ganhou {contador} vezes.')
        break
    if resultado == 'impar' and opcao_cpu in 'Ii':
        print('Você perdeu!')
        print('GAME OVER')
        print(f'Você ganhou {contador} vezes.')
        break
    if resultado == 'par' and opcao in 'Pp':
        print('Você venceu!')
        contador += 1
    if resultado == 'impar' and opcao in 'Ii':
        print('Você venceu!')
        contador += 1
    print('-'*30)
    print('Vamos jogar novamente...')