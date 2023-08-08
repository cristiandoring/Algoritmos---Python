#Mostre a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input('Digite um valor: '))

for i in range(1,11):
    print('{:2} x {} = {:3}'.format(i, numero, numero*i))