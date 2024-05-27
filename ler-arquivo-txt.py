# https://www.hashtagtreinamentos.com/arquivos-de-texto-com-python
# https://pt.rakko.tools/tools/68/

def showTasks():
    print('Todas as Tarefas:')
    arquivo = open("task.txt", "r")
    conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    print(conteudo)
    arquivo.close()  # Não esqueça de fechar o arquivo após a leitura

def showTasksSow():
    # Abre o arquivo em modo de leitura
    with open("task.txt", "r") as arquivo:
        linhas = arquivo.read()
        for linha in arquivo:
            print(linha)

    # Agora 'conteudo' contém todo o texto do arquivo
    print(linhas)