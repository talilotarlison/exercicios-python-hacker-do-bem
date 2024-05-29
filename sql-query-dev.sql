-- create banco
CREATE TABLE dbDevmidia (
  idCliente integer PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sexo CHAR(1) NOT NULL,
  peso DOUBLE,
  dataNascimento DATE
);

CREATE TABLE dbTelefone (
  idTelefone INT PRIMARY KEY,
  ddd INT NOT NULL,
  telefone INT NOT NULL,
  idCliente integer
);
-- https://www.devmedia.com.br/sql-aprenda-a-utilizar-a-chave-primaria-e-a-chave-estrangeira/37636
ALTER TABLE dbTelefone ADD CONSTRAINT idClienteTelefone FOREIGN KEY (idCliente) REFERENCES dbDevmidia (idCliente);

SHOW TABLES;
-- descrição do banco
describe dbDevmidia;
describe dbTelefone;

-- https://medium.com/mandabugs/mysql-tipos-de-dados-introdu%C3%A7%C3%A3o-e-dados-num%C3%A9ricos-1-de-3-a6e48fb5e1d3
-- insert
INSERT INTO dbDevmidia VALUES (1,'joao brito', 'M',1.7,'1974-05-12');
INSERT INTO dbDevmidia VALUES (2,'filho brito', 'M',1.7,'1974-05-12');
INSERT INTO dbDevmidia VALUES (3,'maik brito', 'M',1.7,'1974-05-12');
INSERT INTO dbDevmidia VALUES (4,'pedro brito', 'M',1.7,'1974-05-12');
-- fetch 
SELECT * FROM dbDevmidia;


INSERT INTO dbTelefone VALUES (1,86, 78443547,1);
INSERT INTO dbTelefone VALUES (2,56, 454548789,1);
INSERT INTO dbTelefone VALUES (3,25, 1365489879,4);
INSERT INTO dbTelefone VALUES (4,25, 574687687,4);

SELECT * FROM dbTelefone;

SELECT * from dbDevmidia c, dbTelefone t where c.idCliente = t.idCliente;

SELECT name,ddd, telefone , sexo, peso from dbDevmidia c, dbTelefone t where c.idCliente = t.idCliente;
