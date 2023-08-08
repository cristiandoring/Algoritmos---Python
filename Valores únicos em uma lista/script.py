#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
#únicos digitados, em ordem crescente.

valores = []
while True:
    valor = int(input('Digite um valor: '))

    if len(valores) == 0:
        valores.append(valor)
        print('Elemento adicionado.')
        opcao = input('Quer continuar? [S/N] ')

        while opcao not in 'sSnN':
            print('Opção inválida: ')
            opcao = input('Quer continuar? [S/N] ')

        if opcao in 'Nn':
            print('Encerrando programa.')

            break
    else:
        #laço que percorre cada posição do vetor
        for cada_valor in range(0,len(valores)):
            if valor in valores:
                print('Elemento já existe.')
                break
            else:
                valores.append(valor)
                print('Elemento adicionado.')
                break
        
        opcao = input('Quer continuar? [S/N] ')

        while opcao not in 'sSnN':
            print('Opção inválida: ')
            opcao = input('Quer continuar? [S/N] ')

        if opcao in 'Nn':
            print('Encerrando programa.')

            break
print('Lista em ordem crescente...')

#ordena lista e imprime
valores.sort()
print(valores)

    