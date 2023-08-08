#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* lista):
    lista_ordenada = list(lista)
    lista_ordenada.sort()
    m = lista_ordenada[-1]

    print(f'O maior da {lista} é {m}.')
    print()

maior(3,4,16,5,8,2)
maior(1,2,15)
maior(-4,-5)