show databases;
create database if not exists second_example;
drop database second_example;
use second_example;

CREATE TABLE person(
	person_id SMALLINT UNSIGNED,
	fname VARCHAR(20),
	lname VARCHAR(20),
	gender ENUM('M', 'F'),
	birth_date DATE,
	street VARCHAR(20),
	city VARCHAR(30),
	state VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(20),
	CONSTRAINT pk_person PRIMARY KEY (person_id)
);

CREATE TABLE favorite_food(
	person_id SMALLINT UNSIGNED,
    food VARCHAR(20),
    CONSTRAINT pf_favorite_food PRIMARY KEY(person_id, food),
    CONSTRAINT fk_favorite_food_person_id FOREIGN KEY(person_id) 
    REFERENCES person(person_id)
);
SELECT * FROM favorite_food;
DESC person;

-- Populando o banco de dados
INSERT INTO person VALUES ('2', 'Mariana', 'Ferreira', 'F', '1979-08-21', 
							'Rua Tal', 'Cidade B', 'SP', 'Brasil','04675-120')
                            , ('3', 'Antonia', 'Santos', 'F', '1981-04-29', 
							'Rua Tales', 'Cidade C', 'SP', 'Brasil','04345-180');
SELECT * FROM person;

-- DELETE from person WHERE person_id=1 or person_id=2 or person_id=3;

INSERT INTO favorite_food VALUES(1, 'Lasanha'), 
								(2, 'Feijoada'),
                                (3, 'Mineira');                                ;
SELECT * FROM favorite_food;



-- recuperando as contraints que forma setadas no banco de dados
SELECT * FROM information_schema.table_constraints
WHERE constraint_schema = 'second_example';
-- recuperando de uma tabela
SELECT  * FROM information_schema.table_constraints
WHERE table_name = 'person';

DESC information_schema.table_constraints;