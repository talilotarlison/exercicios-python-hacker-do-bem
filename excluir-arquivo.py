#Claro! Você pode remover uma linha específica de um arquivo de texto em Python de algumas maneiras diferentes. Vou explicar duas abordagens comuns:

#1. **Ler todo o conteúdo, filtrar as linhas e escrever o resultado em um novo arquivo:**
   #Você pode ler todas as linhas do arquivo, filtrar aquelas que não contêm o texto que você deseja excluir e, em seguida, escrever o resultado em um novo arquivo. Aqui está um exemplo de código para fazer isso:


    path = r'Arquivos\\texto.txt'
    texto_procurado = 'Test'

    # Abre o arquivo em modo de leitura
    arquivo_aberto = open(path, 'r')
    todas_linhas = arquivo_aberto.readlines()

    # Filtra as linhas que não contêm o texto procurado
    texto_filtrado = filter(lambda linha: texto_procurado not in linha, todas_linhas)

    # Escreve o resultado em um novo arquivo
    novo_arquivo = r'Arquivos\\resultado.txt'
    with open(novo_arquivo, "w") as output:
        output.write(''.join(list(texto_filtrado)))
 

#2. **Editar o arquivo diretamente sem criar um novo arquivo:**
#   Se você quiser editar o arquivo original diretamente, pode fazer algo como:

    path = r'Arquivos\\texto.txt'
    texto_procurado = 'Test'

    # Abre o arquivo em modo de leitura e escrita
    with open(path, 'r') as arquivo_aberto:
        todas_linhas = arquivo_aberto.readlines()

    # Remove as linhas que contêm o texto procurado
    novas_linhas = [linha for linha in todas_linhas if texto_procurado not in linha]

    # Abre o arquivo novamente em modo de escrita e escreve as novas linhas
    with open(path, 'w') as arquivo_modificado:
        arquivo_modificado.writelines(novas_linhas)
 