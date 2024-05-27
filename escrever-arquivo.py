#Claro! Para escrever na última linha de um arquivo de texto em Python, você pode seguir algumas abordagens diferentes. Vou apresentar duas opções:

#1. **Usando `readlines`, `insert` e `writelines`:**
#   Primeiro, você precisa separar cada linha do seu arquivo. Para fazer isso, utilize o método `readlines`, que retornará uma lista com todas as linhas separadas. Em seguida, insira o texto desejado na posição desejada da lista usando o método `insert`. Por fim, escreva as linhas novamente no arquivo usando o método `writelines`. Veja um exemplo:

    linha_especifica = 1
    texto = "Seu texto aqui"

    with open('arquivo.txt', 'r') as file:
        lines = file.readlines()

    lines.insert(linha_especifica, texto + "\n")

    with open('arquivo.txt', 'w') as file:
        file.writelines(lines)


#2. **Usando um arquivo temporário:**
#   Essa abordagem é mais eficiente para arquivos grandes e evita corrupção do arquivo original. Aqui está um exemplo:


    import shutil
    import tempfile

    def incluir_linha(nome_arquivo, numero_linha, conteudo):
        with open(nome_arquivo) as orig, tempfile.NamedTemporaryFile('w', delete=False) as out:
            for i, line in enumerate(orig):
                if i == numero_linha:
                    out.write(conteudo + "\n")
                out.write(line)

        shutil.move(out.name, nome_arquivo)

    # Exemplo de uso:
    incluir_linha('arquivo.txt', 1, 'Seu texto aqui')

