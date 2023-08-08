#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
#de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
# nas eleições.

from datetime import date
idade = 0
obrigatoriedade_voto = ''
def voto(ano_nasc):
    ano_atual = date.today().year
   
    idade =  ano_atual - ano_nasc
    if idade >0 and idade <16:
        obrigatoriedade_voto = 'NÃO VOTA'
    elif idade >= 16 and idade < 18 or idade > 65:
        obrigatoriedade_voto = 'OPCIONAL'
    elif idade >= 18 and idade <60:
        obrigatoriedade_voto = 'OBRIGATÓRIO'
    
    print(f'Com {idade} anos o voto é {obrigatoriedade_voto}')

    return obrigatoriedade_voto

ano_nasc = int(input('Em que ano você nasceu? '))

voto(ano_nasc)
