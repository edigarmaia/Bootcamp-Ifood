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

SELECT * FROM person;
DESC person;