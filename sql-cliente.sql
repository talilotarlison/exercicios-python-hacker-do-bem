create table Cliente
(
 clienteId integer PRIMARY KEY AUTOINCREMENT ,
 nome VARCHAR(120) not NULL,
 endereco varchar(255),
 cidade varchar(255),
 referencia  varchar(255)
);

create table Produto
(
 produtoId integer PRIMARY KEY AUTOINCREMENT ,
 nome VARCHAR(120) not NULL,
 preco int not null,

);




INSERT INTO nome_tabela (lista-de-campos)
VALUES (lista_dados)

INSERT INTO Produto
VALUES (54546, "Tenis", 53.30)


SELECT nome, cidade FROM CLIENTE
WHERE clienteId = 1

SELECT nome, preco FROM Produto
WHERE produtoId = 54546

SELECT sum(preco) FROM Produto


