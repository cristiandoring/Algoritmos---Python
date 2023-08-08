numero = int(input('Digite um número inteiro:'))

print('Escolha uma das seguintes opções')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input(''))

if opcao != 1 and opcao != 2 and opcao != 3:
    print('Opção inválida!')
elif opcao == 1:
    print('BINÁRIO = ' + bin(numero)[2:])
elif opcao == 2:
    print('OCTAL = ' + oct(numero)[2:])
else:
    print('HEXADECIMAL = ' + hex(numero)[2:])
