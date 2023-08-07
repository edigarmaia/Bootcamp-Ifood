-- create database company;
create schema if not exists company;
use company;

CREATE TABLE employee(
	Fname varchar(15) not null,
    Minit char,
    Lname varchar(15) not null,
    Ssn char(9) not null, 
    Bdate date,
    Address varchar(30),
    Sex char,
    Salary decimal(10,2),
    Super_ssn char(9),
    Dno int not null,
    PRIMARY KEY (Ssn)
);



CREATE TABLE department(
	Dname varchar(15) not null,
    Dnumber int not null,
    Mgr_ssn char(9) not null,
    Mgr_start_date date, 
    PRIMARY KEY (Dnumber),
    UNIQUE (Dname),
    FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn)
);

CREATE TABLE dept_locations(
	Dnumber int not null,
	Dlocation varchar(15) not null,
    PRIMARY KEY (Dnumber, Dlocation),
    FOREIGN KEY (Dnumber) REFERENCES department(Dnumber)
);

CREATE TABLE project(
	Pname varchar(15) not null,
	Pnumber int not null,
    Plocation varchar(15),
    Dnum int not null,
    PRIMARY KEY (Pnumber),
    UNIQUE (Pname),
    foreign key (Dnum) references departament(Dnumber)
);

CREATE TABLE works_on(
	Essn char(9) not null,
    Pno int not null,
    Hours decimal(3,1) not null,
    PRIMARY KEY (Essn, Pno),
    FOREIGN KEY (Essn) references departament(Ssn),
    FOREIGN KEY(Pno) references project(Pnumber)
);
DESC dependent;

CREATE TABLE dependent(
	Essn char(9) not null,
    dependent_name varchar(255) not null,
    Sex char,
    Bdate date,
    Age int,
    Relationship varchar(8),
    PRIMARY KEY (Essn, dependent_name),
    FOREIGN KEY (Essn) references employee(Ssn)
);
