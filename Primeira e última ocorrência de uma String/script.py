#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))

#find retorna a primeira ocorrência e rfind a última ocorrência
print('A primeira vez apareceu na posição {} e a última na posição {}.'.format(frase.find('A')+1,frase.rfind('A')+1))