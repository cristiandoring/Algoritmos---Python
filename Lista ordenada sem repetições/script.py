#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []

for i in range(0,5):
    
    valor = int(input('Digite um valor: '))

    #verifica se é primeiro elemento ou o ultimo e add
    if i == 0 or valor > valores[-1]:
        valores.append(valor)
        print('Elemento adicionado ao final da lista.')
    #verifica qual posicao vai adicionar no meio da lista
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                #insere o valor atual na posicao da lista
                valores.insert(posicao,valor)
                print(f'Elemento adicionado na posição {posicao}.')
                break
            posicao += 1




print('='*30)
print('{:^30}'.format('LISTA CRESCENTE'))

print(valores)
print('='*30)
