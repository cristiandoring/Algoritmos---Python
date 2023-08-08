#Faça um programa que o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar 
#adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
i = 1
print('SOU SEU COMPUTADOR...')
print('Acabei de pensar em um número de 1 a 10.')
print('Será que você consegue adivinhar qual foi?')
numero_digitado=0
contador = 0
#sorteia numero aleatorio
numero_sorteado = random.randint(1,10)

while numero_digitado != numero_sorteado:
    numero_digitado = int(input('Digite um número de 1 a 10: '))
    contador += 1

    if numero_sorteado > numero_digitado:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente um número menor.')
print('Acertou com {} tentativas. PARABÉNS!'.format(contador))