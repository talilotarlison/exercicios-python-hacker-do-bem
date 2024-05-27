# main.py
#https://pt.stackoverflow.com/questions/76428/como-gerar-n%C3%BAmeros-aleat%C3%B3rios-em-python
from random import randint

#https://diveintopython.org/pt/learn/classes/object-instantiation
# https://horadecodar.com.br/como-limitar-numeros-decimais-em-python/
#https://blog.michelelozada.com.br/como-delimitar-casas-decimais-em-python/
#https://www.askpython.com/python/array/python-add-elements-to-an-array

def main():
   
    
    class Produto:
        def __init__(self,nome, marca, preco, garantia,pais_fabricacao):
            self.nome = nome
            self.marca = marca
            self.preco =  preco
            self.garantia = garantia
            self.pais_fabricacao = pais_fabricacao
            
        def getProduto(self):
            novoProduto = {'nome': self.nome, 'marca': self.marca, 'preco' : round(self.preco,2), 'garantia': self.garantia , 'pais_fabricacao' : self.pais_fabricacao}
            return novoProduto
    
    meu_estoque = []

    class AdcionarProdutoNoEstoque:  
        def __init__(self, categoria,quantidade, data_entrada, produto):
            self.categoria = categoria
            self.quantidade = quantidade
            self.data_entrada = data_entrada
            self.produto = produto
        
        def addNoEstoque(self):
            produto = Produto(self.produto['nome'], self.produto['marca'],self.produto['preco'] , self.produto['garantia'],self.produto['pais_fabricacao'])
            add_produto = { 'id': randint(0,99999),'categoria' : self.categoria , 'data_entrada': self.data_entrada , 'quantidade': self.quantidade,'produto': produto.getProduto()}
            meu_estoque.append(add_produto) 

        def getEstoque(self):
            return meu_estoque
        

    cadeira = AdcionarProdutoNoEstoque('Moveis', 4,'18/05/2024',{'nome' : 'Cadeira','marca' :'Madereira','preco':200.99,'garantia':False,'pais_fabricacao' :'BR'})
    cadeira.addNoEstoque()

    notebook = AdcionarProdutoNoEstoque('Eletronicos', 14,'18/05/2024',{'nome' : 'Notebook L15','marca' :'Asus','preco':1700.99,'garantia':True,'pais_fabricacao' :'EUA'})
    notebook.addNoEstoque()

    print(notebook.getEstoque())


if __name__ == "__main__":
    main()
