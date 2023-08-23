create database oficina;

use oficina;

create table cliente(
	id_cliente int primary key auto_increment,
    nome varchar(255) not null,
    contato varchar(25)
);
select * from cliente;
insert into cliente (nome, contato) values ('Cida', '11 9972-7546'), ('Maria', ' 3652-4576'), ('Ana', '3645-2673');


create table veiculo(
	id_veiculo int primary key auto_increment,
    id_cliente int,
    marca varchar(100) not null,
    modelo varchar(100) not null,
    foreign key (id_cliente) references cliente(id_cliente)
);
select * from veiculo;
insert into veiculo (id_cliente, marca, modelo) values (1, 'Fiat', 'bravo'),(2,'VW', 'jetta'), (3,'GM', 'corsa');


create table servico(
	id_servico int primary key auto_increment,
    descricao_servico varchar(255),
    preco decimal(10,2)
);
select * from servico;
insert into servico (descricao_servico, preco) values ('troca bandeja', 150.00), ('troca velas', 50.00),('alinhamento', 45.00);

create table peca(
	id_peca int primary key auto_increment,
    desc_peca varchar(255) not null,
    preco_peca decimal(10,2)
);
select * from peca;
insert into peca (desc_peca, preco_peca) values ('bucha bandeja',35.00), ('jogo de velas', 88.00);

create table itemServico(
	id_item int primary key auto_increment,
    id_servico int,
    id_peca int,
    quantidade int,
    foreign key (id_servico) references servico(id_servico),
    foreign key (id_peca) references peca(id_peca)
);
select * from itemServico;
insert into itemServico (id_servico, id_peca, quantidade) values (1,3,1), (2,1,3), (3,2,1);

-- recupera nome do cliente, marca e modelo do seu veiculo
select c.nome as Nome_Cliente, v.marca as Marca, v.modelo as Modelo from cliente c
inner join veiculo v on c.id_cliente = v.id_cliente;

-- recupera o nome de uma peça
select * from peca where id_peca=1;  

-- recupera veiculo com modelo terminados com as letras ta
select * from veiculo where modelo like '%ta';

-- recupera nome e quantidade do serviço, nome da peça e valor unitario
select s.descricao_servico as Descricão, i.quantidade as Quant, p.desc_peca  as Peça, p.preco_peca as Preço from servico s
inner join itemServico i on s.id_servico = i.id_servico
inner join peca p on p.id_peca = i.id_peca;