#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
#fechados na ordem correta.

parentese_aberto = parentese_fechado = 0
parenteses = []
expressao = str(input('Digite a expressão: '))

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
    
if len(parenteses) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')


