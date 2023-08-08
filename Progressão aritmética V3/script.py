#Faça um programa que pergunte para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)

termo1 = int(input('Digite o primeiro termo: '))
termo = termo1
razao = int(input('Digite a razão: '))
quantidade_termos = 1

print(termo1, end=' -> ')

for i in range (1,10):
    termo = termo + razao
    print(termo,end=' -> ')
    quantidade_termos += 1
print('PAUSA')
while True:

    opcao = int(input(('Quantos termos você quer mostrar a mais? ')))
    if opcao == 0:
        print('Progressão finalizada com suceso.')
        print('Quantidade de termos impressos foi de {}.'.format(quantidade_termos))
        break
    else:
        for j in range (0,opcao):
            termo = termo + razao
            print(termo,end=' -> ')
            quantidade_termos += 1
        print('PAUSA')
