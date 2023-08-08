#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1                  
#b) de 10 até 0, de 2 em 2                                                                                                                                            
#c) uma contagem personalizada
from time import sleep

def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}.')

    if c <0:
        c = abs(c)
    if c == 0:
        c = 1
    if a < b:
        for i in range(a,b+1,c):
            print(i,end=(' '),flush=True)
            sleep(0.5)
        print('FIM')
        print()
    elif a > b:
        for i in range(a,b-1,-c):
            print(i,end=(' '),flush=True)
            sleep(0.5)
        print('FIM')
        print()

inicio = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('Pulo: '))

contador(1,10,1)
contador(10,0,2)
contador(inicio,fim,pulo)
