#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'ESTUDAR', 'TRABALHAR', 'PRATICAR', 'PYTHON')

for i in palavras:
    print(f'Na palavra {i} temos', end=' ')

    for letras in i:
        if letras in 'aeiouAEIOU':
            print(f'{letras}',end=' ')
    print()