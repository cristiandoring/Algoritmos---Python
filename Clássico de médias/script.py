nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2:'))
nota3 = float(input('Digite a nota 3:'))

media = (nota1 + nota2 + nota3)/3

if media >=7:
    print('APROVADO')
elif media >=0 and media < 5:
    print('REPROVADO')
else:
    print('EM RECUPERAÇÃO')