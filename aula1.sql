
-- create
CREATE TABLE Aluno (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');

-- fetch 
SELECT * FROM EMPLOYEE WHERE dept = 'Sales';

-- testes da aula

-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales');

-- fetch 
select * from EMPLOYEE;

DESCRIBE EMPLOYEE;

CREATE TABLE aluno (
  id INTEGER PRIMARY KEY,
  name varchar(100) NOT NULL,
  city varchar(100) NOT NULL
);


insert into aluno VALUES(1,'talilo', 'cocal dos alves');
insert into aluno VALUES(2,'mario', 'cocal dos alves');

select * from aluno;

alter table   aluno
drop column  city;

select * from aluno;


alter table   aluno
add column  cidade varchar(100);

select * from aluno;


alter table   aluno
rename column  cidade to cidades ;

select * from aluno;

DESCRIBE aluno;
