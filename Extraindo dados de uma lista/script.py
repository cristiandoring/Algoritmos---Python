#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.                                                                                                          
#B) A lista de valores, ordenada de forma decrescente.                                                                                          
#C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
contador_elementos = 0

while True:
    valores.append(int(input('Digite um valor: ')))
    contador_elementos +=1
    opcao = str(input('Quer continuar? [S/N]'))

    while opcao not in 'SsNn':
        print('Opção inválida.')
        opcao = str(input('Quer continuar? [S/N]'))
    if opcao in 'nN':
        break

#ordena a lista em ordem decrescente
valores.sort(reverse=True)

print('='*30)
print(f'Você digitou {contador_elementos} elementos.')
print(f'Os valores em ordem decrescente são {valores}.')

if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')