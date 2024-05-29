CREATE table cursos(
  id integer no NULL PRIMARY KEY,
  nome char[50]
);


CREATE TABLE aluno(
 cpf char[11] NOT NULL PRIMARY KEY,
 nome varchar[150],
 data DATA,
 id_cursos integer,
 CONSTRAINT aluno FOREIGN KEY (id_cursos) REFERENCES cursos (id)
);

INSERT into cursos VALUES(0 , "Historia");
INSERT into cursos VALUES(1, "Biologia");
INSERT into cursos VALUES(2, "Geografia");

SELECT * from cursos;

SELECT * from aluno;



drop table cursos;


INSERT INTO aluno VALUES("15736786", " Bruno", "1998-02-02", 2);
INSERT INTO aluno VALUES("154636786", " Fabio", "1990-02-02", 2);
INSERT INTO aluno VALUES("157736786", "Claudio", "1999-02-02", 2);