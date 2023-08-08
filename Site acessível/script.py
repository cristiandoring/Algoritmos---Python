# Crie um código em Python que teste se o site pudim (http://www.pudim.com.br/) 
#está acessível pelo computador usado.

import requests

def teste(site_url):
    try:
        # Fazendo uma requisição GET para o site
        response = requests.get("http://www.pudim.com.br/"  )
    except:
           #se não conseguir a requisição, ele retorna essa mensagem
           print("URL indisponível.")
    else:
        print('O site está acessível.')

#chama função com o parâmetro sendo a url
teste("http://www.pudim.com.br/"  )