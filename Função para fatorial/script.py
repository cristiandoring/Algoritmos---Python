#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o 
#número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado 
#ou não na tela o processo de cálculo do fatorial.

def fatorial(numero,show=False):
    resultado = 1
    
    for i in range(numero,0,-1):
        resultado *= i
    
    if show == True:
        for j in range(numero,0,-1):
            print(j,end='')
            if j > 1:
                print(end=' x ')
            else:
                print(' = ',end='')

    return resultado
    
print(fatorial(3, True))