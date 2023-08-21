-- criação do bando de dados para o cenário de um ecommerce.

create database ecommerce;
use ecommerce;

-- tabela cliente
create table clients(
	idClient int auto_increment primary key,
    Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30),
    constraint unique_cpf_client unique (cPf)
);
-- tabela produto
create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10) not null,
    classification_kids bool default false,
    category enum('eletrônico', 'Vestimenta', 'Brinquedos', 'Alimentos', 'Móveis') not null,
    assessment float default 0,
    size varchar(10)
);
-- tabela pedido
create table orders(
	idorder int auto_increment primary key,
	idorderClient int,
	orderStatus enum('cancelado', 'Confirmado', 'Em processamento') default 'em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash boolean default false, 
    constraint fk_ordes_client foreign key (idorderClient) references clients(idClient)
			on update cascade
);
-- tabela pagamentos
create table payments(
	idclient int,
    idPayment int,
    typePayment enum('boleto','Cartão','Dois cartões'),
    limitAvailable float,
    primary key(idClient, idPayment)
);

-- tabela estoque
create table productStorage(
	idProdStorage int auto_increment primary key,
	storageLocation varchar(255),
    quantity int default 0
);

-- tabela fornecedor
create table supplier(
	idSupplier int auto_increment primary key,
    SocialName varchar(255) not null,
    CNPJ char(15) not null,
    contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
);

-- tabela vendedor
create table seller(
	idSeller int auto_increment primary key,
    SocialName varchar(255) not null,
    AbstName varchar(255),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_spf_seller unique (CPF)
);

-- tabela produto vendedor
create table productSeller(
	idPseller int,
    idProduct int,
    Quantity int default 1,
    primary key (idPseller, idProduct),
    constraint fk_product_seller foreign key (idPseller) references seller(idPseller),
    constraint fk_product_product foreign key (idProduct) references product(idProduct)
);










