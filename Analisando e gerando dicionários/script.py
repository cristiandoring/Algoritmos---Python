#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um 
#dicionário com as seguintes informações:
#A) Quantidade de notas
#B) A Maior nota
#C) A média da turma
#D) A situação (opcional)
def notas(*n,situacao=False):
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/len(n)
    
    if situacao:
        if dicionario['media'] < 5:
            dicionario['situacao'] = 'PÉSSIMO'
        elif dicionario['media'] > 5 and dicionario['media'] <7:
            dicionario['situacao'] = 'RAZOÁVEL'
        else:
            dicionario['situacao'] = 'BOA'
    return dicionario

resultados = notas(10,8,situacao=True)
print(resultados)