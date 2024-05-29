-- https://learnsql.com.br/blog/como-usar-um-coringa-sql/
-- create
CREATE TABLE Tarefas (
  Id INTEGER PRIMARY KEY AUTO_INCREMENT,
  titulo TEXT NOT NULL,
  texto TEXT NOT NULL
);

-- insert
INSERT INTO Tarefas VALUES ( 0,'Cursps', 'fazer curso de hardware');
INSERT INTO Tarefas VALUES ( 0,'Cursos', 'fazer curso de SO');

-- fetch 
SELECT * FROM Tarefas where texto like "%so";
