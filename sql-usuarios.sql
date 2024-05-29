CREATE table if not EXISTS usuario (
	id INT(11) NOT NULL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL DEFAULT '',
    nasciento DATE,
    estudante NOT NULL DEFAULT "N",
    cadeira int(4)
   )
   
   INSERT INTO usuario(id, nome,nasciento, estudante, cadeira)
   VALUES(2232123, "joao filho","200-01-01","S", 22)
   
   SELECT * from  usuario;


  
create table if not exists produto(
codPro int(10),
nome varchar(50),
categoria varchar(50),
preco int(10)
);

ALTER TABLE produto  MODIFY COLUMN preco decimal(2.5);
   
--As técnicas SQL denominadas JOIN possibilitam efetuar consulta em duas tabelas ou mais, dependendo da necessidade da busca. 