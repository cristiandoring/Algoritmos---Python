# Modifique as funções que foram criadas no desafio formatando moedas  para que elas aceitem um parâmetro 
#a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()

import moeda
import resumo

preco = float(input('Digite um preço: R$ '))

#chama a função resumo salva na biblioteca(arquivo) 'resumo'
resumo.resumo(preco)