def leiaDinheiro(mensagem):
    valido = False
    while not valido:
        entrada = input(mensagem).replace(',','.').strip()
        
        #se for texto ou se for vazio ele mostra erro e pede pra digitar novamente
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! {entrada} é um preço inválido.')
        else:
            valido = True
            return float(entrada)
