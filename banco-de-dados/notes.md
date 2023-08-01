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
Conceitual --> Lógico --> Físico


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









































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       






