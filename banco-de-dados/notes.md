# Banco de dados

## SGBD
Definição - tipo de dados
Contrução - inserção de dados
Manipulação - recuperação, relatórios
compartilhamento - acesso, simultaneidade

Ciclo de vida longo
Proteção
### Mais utilizados
1 - Oracle
2 - MySQL
3 - SQL Server
4 - PostgreSQL
5 - MongoDB
6 - Redis
7 - ElasticSearch
9 - Access
11 - Cassandra
12 - MariaDB

## Histórico
SGBD 1960, IBM para diminuir custos com pessoal, inconsistência de dados;
Modelo relacional 1970, por Ted Codd, IBM, baseado na álgebra relacional, teoria de conjuntos;
DB Honeywell, 1976 não relacional
Oracle 2, 1980 relacional
Oracle 3, 1983

### Modelo Relacional
* Definição das tabelas e constrains para dados
* Comandos traduzidos pelo processador LDD(linguagem de definição de dados)

### Porque usar SGBD?
Abstração
Auto-descrição
Isolamento
Compartilhamento
Múltiplas visões
Transação multiuser

## Atores
### DB Designer
* Identificar os dados e requisitos
* Representação e estrutura
* Fase preliminar

### DBA - Administrador do banco de dados
* Gerencia Recursos
* Orquestração do sistema
* Autorização de acesso

### Usuários finais
* Consumir as informações

Acessos:
Casuais
	Acessos ocasionais, diferentes informações, uso de APIs

Ingênuos
	Considerável porção
	Canner transactions - criadas por engenheiros de software
	Erro: raro

Sofisticados
	Conhecimento prévio do sistema, engenheiro, analista

Standalone
	BD pessoal


Finalidade o SGBD
Implementar diversas facilidades para os usuários

### Ganhos com SGBD
1 - Padronização
2 - REdução de tempo no desenvolvimento da aplicação
3 - Flexibilidade
4 - Disponibilidade de info atualizadas
5 - Economia com escalabilidade

## Modelagem de dados
Possui foco na descrição e relacionamento dos elementos que compõem a representação do contexto (mini-mundo)
* Conceitual -> representação gráfica
* Físico - > parte da implementação do sistema

Mini-mundo - delimita o contexto dos dados
Alto nível - requisitos para criação do modelo
Esquema - definido estrutura relacional, facilita a compreensão do contexto dos dados, entidade-relacionamento e UML
SGBD - implementando, criando o BD

## MYSQL
Comandos
create database - cria o banco
show databases - mostra os bancos
use - entra no banco específico
drop - deleta

## Arquitetura de Banco de Dados
Abstração = essencial

Classificação
Modelo de dados físico - especialista
Modelo de dados conceitual - visão de alto nível
	entidade
	atributos
	relacionamentos
	MER
	generalização
	especialização
	
Modelo de dados de implementação - representacional
	constrains
	modelo de dados relacional
	modelos hierárquicos
	operações
	linguagens
	
## Esquemas, Instancias e Estados do BD
Esquema - descrição, o que tem lá e de atributos e objetos e como eles interagem entre si;
Meta dados - snapshot com toda estrutura que o banco de dados está mantendo, descrição esquema, contrutores e constrains

## Arquitetura three-schema
Características
Catálogo
Isolamento data/program
Views

External level
	external/conceitual
	mapeamento
	
Conceptual level
	conceitual/interno
	mapeamento
Internal level

Promover um isolamento de tal forma que, a modificação que ocorra em um determinado schema não influencie o schema subsequente;

# Introdução a modelagem de banco de dados

* Mundo fechado
			Preposição
		Lógica formal do sistema que vai além do BD
	Predicado
	
		
## Algebra relacional
Linguagem formal para consulta/extração de dados
O predicado é a parte da oração que contém o verbo e que traz informações sobre o sujeito.
Lógica de predicados
	critério	having / where	
any, max, avg, count, sum, min
				 
algebra relacional --> sgbd --> resultado da ação

## Modelagem
Conceitual - o que vai ter
Lógico - como estruturar
Físico - como implementar


### Design de BDs - Projeto conceitual
Linguagens de modelagem de dados - representação
	Gráficas
	Textuais

Requisitos, perguntas a serem respondidas, visões...
	Coleta de dados
	Análise
Esquema conceitual
Modelo Entidade Relacionamento
UML - Diagrama de Classes
Requisitos funcionais da aplicação
Modelo de alto nível

Requisitos funcionais
	O que executar? Quais processos?

Requisitos não funcionais
	Segurança, desempenho ...
	
### Projeto lógico
Descrição do modelo conceitual
Organização dos dados
Estrutura
Esquema do banco de dados
Criação do esquema lógico

Entidade fraca, precisa de outra entidade para existir

### Projeto físico
Descrição do modelo conceitual
Como será implementado?
* estrutura e índices
* organização e caminhos de arquivos
* segurança, performance ...
Diretamente ligado ao SGBD
Alocação de memória
Particionamento de tabelas

## Modelo Entidade Relacionamento - MER
Projeto conceitual, alto nível, dominio do negócio
A instância é um conjunto de entidades
Representado em um diagrama de entidade relacionamento - DER
	Diagrama ER
		Raras modificações
		Facilidade de manipular
		Esquema ER do banco de dados

Notações:
	Entidades: classes/objetos -> retangulo
	Relacionamento: agregações -> losango
	Atributos: propriedades elementares -> elipse conectada por uma haste
	Entidades fracas e relacionamentos -> com linha dupla
	Chave parcial -> linha pontilhada
	Chave principal -> linha contínua
	Dependência de existência -> || pipe duplo
	Atributo derivado -> elipse pontilhada
	Atributo composto -> várias elipses ligadas a uma central
	
- Tipos de entidades
	Componente básico
	Existencia independente
	Atributos
	Entidades <------------> Objetos

 - Entidade fraca
 	Só existe se estiver relacionada a outra entidade (forte, regular)
 	Chave não obrigatória
 	Dependência
 	Exclusão cascata
 	Ex: Empregado -> dependente, o dependente só existe enquanto o empregado existir
 	
 - Atributos e chaves
   Atributos
   	Características/descrição das entidades
   	Atributos relacionados as instâncias
   	
   	Atômicos x compostos(atributos que compoem um atribuito, ex: nome (nome + sobrenome))
   	Atributos multivalorados (tem intervalo)
   	Armazenados (não modificam, ex: data aniversário) e derivados
   	Atributos nulos
   	Atributos complexos

 - Relacionamentos
	Baseado na teoria de conjuntos
	Classificados por:
	Grau 
	Auto-relacional ou não 
	Cardinalidade
	Relacionamento como atributo
	
 - Constraints - cardinalidade
 	Cardinalidade corresponde ao nº máximo de instâncias que participam de um determinado relacionamento. Ex: 1:1, 1:N, N:1 ...


UML - linguagem para desenvolvimento de software
Trabalha com visões: interpretada e construída

Compreensão facilitada
Liberdade para o desenvolvedor
Orientação à objetos
Visão lógica
Visão de casos de uso
Visão de processo
Visão de implantação
Visão de implementação

Classes(entidade)
Orientado a objetos
Atributos
Operações
Associações(relacionamento)

Relacionamentos
Associação
Agregação

Relacionamentos de alto grau
Ternário, ..., N-nário
Perspectiva diferente do binário


Papéis e constraints
Esquema relacional
Diagrama ER

## Modelo EER
Novos conceitos semanticos
Desenvolvimento fora da área de BDs
Diagrama EER
Entidade ----> Objeto

A especialização está relacionada a subclasses, pois está especificando algo. Gera subclasses.
Generalização, o inverso da especialização, propriedades comuns as entidades. Gera superclasses.


### Superclasses
comportamento e estado gerais


### Herança
classe filha herda atributos e comportamentos da classe mãe
Principio próprio à programação orientada a objetos (POO) que permite criar uma nova classe a partir de uma já existente;
Reutilização de código
Agregar atributos e métodos
Especialização de classes


### Subclasses
Comportamento e estado específicos
Depende do contexto do BD
Objeto distinto no BD


Constraints - Regras
Deletar
	Superclasse -> subclasse
	
Inserção
	Entidade em superclasse -> predicated-defined
	Entidade em superclasse com total -> subclasse macth

### Hierarquia e rede de especialização
Hierarquia de especialização
Uma subclasse pode ter apenas um pai

Requisitos
Rastreamento das 3 entidades e overlaping de entidades
Tipos definidos de empregados
Informação dos alunos - grau academico
Estudantes graduandos ou não


Union type
Coleção de objetos de diferentes tipos de entidades
Repersentação: subclasse


## Modelo Relacional e Mapeamento ER/Relacional

DDL - data definition language -> create, drop, insert, rename ...
DML - data manipulation language -> insert, update, delete, merge
DCL - data control language -> grant, revoke
DQL - data query language -> select

Integridade
Como manter um estado válido?
 * Constraints de integridade
 * Constraints de domínio, chave, Not Null
 Integridade de entidade
 Integridade referencial

Algoritmo de mapeamento
 * Atributos de valor único (single-values)
 * PK - Primary Key & Unique Key
 * Constraint de Entidade e Referencial
 
# Explorando a SQL
## Tipos de dados

char - tamanho fixo
varchar - tamanh variável
tinytext
text
mediumtext
longtext
conjunto de caracteres - show caracter set
tinyint
smallint
mediumint
int
bigint
float
double
date
datetime
timestamp
year
time

## Constraint

Not null -> não permite valor nulo na tabela
Pk - chave primaria
fk - chave estrangeira
default - valor padrão
delete - remover um registro do banco de dados
unique - torna unico
distinct - retorna apenas uma ocorrência


SELECT <lista de atributos> FROM <tabela> WHERE <condição>;

DML 
INSERT INTO <table> (<lista-atributos>) VALUES (<lista-valores>);


*****************************************************************
# Explorando comandos DDL - data definition language
update - modifica a partir de uma condição
update <nome_tabela>
	set coluna1 = valor1, coluna2 = valor2, ...
	where condição;
drop - remoção de estruturas
drop database <nome_do_banco>;	

delete - remoção de registros
delete from <nome_tabela> where condição;

alter - modificação da estrutura do banco de dados
alter table <nome_tabela> add <nome_campo + tipo_de_dado>; 

## Agrupamento de registros
count - registros
sum - somatório
min - valor mínimo - atributo
max - valor máximo - atributo
average - media de valor - atributo


# Agrupando registros e tabelas com JOIN

### Case statement
* troca de um valor
* condição para troca
* mapeamento de valores de correspondência

case { when - quando algo acontece
	then - então faça alguma ação
	} end
similar ao switch case

Exemplo
UPDATE tabela_funcionario SET salario = 
	CASE
	   WHEN depto = 5 THEN salario + 2000
      	   WHEN depto = 4 THEN salario + 1500
     	   ELSE salario + 0
	END; 

### Agrupamento com CASE
SELECT year,
CASE
WHEN wind_speed >= 40 THEN 'high'
WHEN wind_speed >= 30 THEN 'moderate'
ELSE 'low'
END as wind_severity,
COUNT(*) as record_count
FROM station_data
GROUP BY 1,2;

### Caso zero/null trick
* filtros - valores distintos
* select query

Exemplo SEM O CASE
SELECT year, month,
SUM(precipitation) AS tornado_precipitation
FROM station_data
WHERE tornado = 1
GROUP BY year, month;


Exemplo COM O CASE
SELECT year, month,
SUM(CASE WHEN tornado = 1 THEN precipitation ELSE 0 END)
AS tornado_pecipitation,
SUM(CASE WHEN tornado = 0 THEN precipitation ELSE 0 END)
AS non_tornado_precipitation
FROM station_data
GROUP BY year, month;


### Multiplas tabelas com JOINs
INNER JOIN
* mais comum dos JOINs
* linhas não correspondentes excluídas
* atributo de junção

SELECT <lista de atributos>
FROM <tabela1> as alias
INNER JOIN <tabela2> as alias2
ON <atributos de junção "a.t = b.t">;


SELECT e.fname, e.lname, d.name
FROM employee e 
INNER JOIN department d
ON e.dept_id = d.dept_id;

SELECT Fname, Lname, Address
     FROM (employee join department on Dno = Dnumber)
     WHERE Dname = 'Research';

SELECT Dname AS Department, Dept_create_date AS StartDate, Dlocation AS Location
      FROM department JOIN dept_locations using (Dnumber) -- using quando o atributo de junção tiver o mesmo nome nas duas tabelas
      ORDER BY StartDate;

* INNER JOIN entre 3 ou + tabelas
SELECT * FROM employee
     INNER JOIN works_on ON Ssn = Essn
     INNER JOIN project ON Pno = Pnumber
     ORDER BY Pnumber;

-- project, works_on e employee     
SELECT concat(Fname, ' ', Lname) AS Complete_name, Dno As Dept_number, Pname AS Project_name, Pno AS Project_number, Plocation As Project_location FROM employee
     INNER JOIN works_on ON Ssn = Essn
     INNER JOIN project ON Pno = Pnumber
     WHERE Pname LIKE 'Product%'
     ORDER BY Pnumber;                              

-- department, dept_location, employee
SELECT Dnumber, Dname, concat(Fname,' ',Lname) AS Manager, Salary, round(Salary*0.05,2) AS Bonus FROM department
     INNER JOIN dept_locations using (Dnumber)
     INNER JOIN employee ON Ssn = Mgr_ssn
     GROUP BY Dnumber;

### NATURAL JOIN
* condição de junção implícita
* atributos comuns

SELECT Fname, Lname, Address
   FROM (employee NATURAL JOIN
        (department AS Dept (Dname, Dno, Mssn, Msdate)))
   WHERE Dname = 'Research';



















































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       






