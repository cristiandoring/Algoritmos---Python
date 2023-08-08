#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idade_homem_mais_velho = 0
mais_velho = ''
somatorio_idades = 0
contador_mulheres = 0

for i in range(1,5):
    
    nome = input('Digite o nome da {}º pessoa: '.format(i))
    idade = int(input('Digite a idade da {}º pessoa: '.format(i)))
    sexo = input('Digite o sexo (f/m) da {}º pessoa: '.format(i))
    somatorio_idades += idade
    if i == 1 and sexo in 'Mm':
        mais_velho = nome
        idade_homem_mais_velho = idade

    if idade > idade_homem_mais_velho and sexo in 'Mm':
        mais_velho = nome
        idade_homem_mais_velho = idade

    if sexo in 'Ff' and idade < 20:
        contador_mulheres += 1

print('A media de idades é {}.'.format(somatorio_idades/4))
print('O homem mais velho é {}.'.format(mais_velho))
print('A quantidade de mulheres menores de 20 é {}.'.format(contador_mulheres))
    

