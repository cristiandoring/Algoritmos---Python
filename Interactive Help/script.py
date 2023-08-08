#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
# manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 

def ajuda(entrada):
    print(f'Acessando manual do {entrada}.')
    help(entrada)

entrada = ''


while True:
    entrada = input('Digite o comando que deseja acessar: ')
    if entrada.upper == 'FIM':
        break
    else:
        ajuda(entrada)
print('FINALIZANDO...')
