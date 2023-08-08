lista_pessoas = []
#verifica se o arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#cria um arquivo 
def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')

#mostra o conteúdo do arquivo
def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n','')
            print(f'{dados[0]:<30}{dados[1]:>3} anos.')
            
    finally:
        a.close()
     

def cadastrar(arq, nome='<desconhecido>',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Falha ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Falha ao cadastrar usuário.')
        else:
            print('Usuário cadastrado.')
            a.close()
    