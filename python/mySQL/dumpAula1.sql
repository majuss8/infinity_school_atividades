-- DDL => Data Definition Language
-- CREATE ALTER DROP

-- Como criar um banco de dados?
CREATE DATABASE escola;

-- Como apagar um banco de dados?
DROP DATABASE escola;

-- Como criar uma tabela?
USE escola;

CREATE TABLE alunos(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    idade INT,
    curso ENUM('Java', 'Python', 'Javascript', 'Node', 'c--'), -- só armazena esses valores nessa coluna
    nota FLOAT
);

DESCRIBE alunos;

-- 1. Crie um banco de dados chamado loja
create database loja;

-- 2. Selecione o banco de dados usando o comando USE
use loja;

-- 3. Crie uma nova tabela chamada produtos com os campos (codigo, nome, preco, categoria, quantidade em estoque)
create table produtos(
	codigo INT PRIMARY KEY AUTO_INCREMENT, 
    nome varchar(150) not null, 
    preco float, 
    categoria varchar(150), 
    quantidade_em_estoque int
);

-- 4. Crie uma nova tabela chamada funcionarios com os campos (id, nome, setor, salario)
create table funcionarios(
	id INT PRIMARY KEY AUTO_INCREMENT, 
    nome varchar(150) not null, 
    setor varchar(150), 
    salario float
);

-- 5. Crie uma nova tabela chamada clientes com os campos (id, nome, endereco, telefone)
create table clientes(
	id INT PRIMARY KEY AUTO_INCREMENT, 
    nome varchar(150) not null, 
    endereco varchar(200), 
    telefone varchar(20)
);

-- 6. Use o comando drop para apagar a loja
drop database loja;





