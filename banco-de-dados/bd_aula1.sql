CREATE DATABASE firstExample;

USE firstExample;

CREATE TABLE periodicos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome_periodico VARCHAR(20),
    issn INT UNIQUE,
    id_editora INT
);

CREATE TABLE editora(
	id INT AUTO_INCREMENT,
    nome_editora VARCHAR(120) UNIQUE,
    pais VARCHAR(5),
    PRIMARY KEY(id)
);

ALTER TABLE periodicos ADD CONSTRAINT fk_editora_periodico FOREIGN KEY (id_editora) REFERENCES editora(id);
INSERT INTO editora(nome_editora, pais) VALUES ('IEEE', 'EUA'), ('DataScienceMagazine', 'EUA');
SELECT * FROM editora;

INSERT INTO periodicos (nome_periodico, issn, id_editora) VALUES ('Special Issue', '12457937', '1');
SELECT * FROM periodicos;

SHOW TABLES;