# Tecnicas de Machine Learning
## ETL
É um tipo de data integration em três etapas (extração, transformação e carregamento) comumente usado para construir um data warehouse.

Extract - extrair
Consiste em se comunicar com outros sistemas ou bancos de dados para capturar os dados que serão inseridos no destino, seja um staging area ou outro sistema;
	Importar dados de diversos tipos e formatos como:
	Pasta de trabalho, diversos bancos de dados, csv, txt, json, etc.
	
	
	
Transform - transformar
É composto por várias etapas: padronização, limpeza, qualidade. Dados vindos de sistemas diferentes tem padrões diferentes, seja de nomenclatura ou mesmo de tipos de dados;
	Colunas, linhas
	Tipos de dados
	Mesclar, acrescentar
	Listas, tabelas


Load - carregamento
É a etapa final onde os dados são lidos das áreas de staging e preparação de dados, carregados no Data Warehouse ou Data Mart Final;
	Para o modelo de dados
	

Algumas vantagens para ETL
Metadados gerados de forma automática, evitando probelmas na geração de informaçõs incorretas
Performance, suporte para carregar dadoss com maior velocidade e usando menos recursos
Pode ser deslocada e distribuida entre servidores mais facilmente
Reinicialização, ferramentas que possuem a capacidade de reiniciar a carga de onde pararam sem a necessidade de codificação
Segurança e estabilidade, é possível articular melhor a segurança tornando-a mais modular, dividindo as finalidades(criação de cargas, execução de cargas, agendamento, etc.)

Principais ferramentas
IBM Data Stage
Power Center
Sql Server Integration Services
Talend ETL

## Biblioteca Pandas
Permite trabalhar com diferentes tipos de dados

Serie é uma matriz unidimensional que contém uma sequência de valores que apresentam uma indexação de números inteiros ou rótulos, muito parecida com uma única coluna do excel.

DataFrame é uma estrutura de dados tubular, semelhante a planilha de dados do excel, em que tanto as linhas quanto as colunas apresentam rótulos.

### Comandos
df.shape() -> retorna volume de informação estrutural.
df.info() -> rotorna o formato dos dados em cada coluna elém da quantidade de memória. 
df.isnull().sum() -> verifica quantos dados altantes existem em nosso conjunto.
df['setor'].unique -> verifica quais os valores únicos existem na coluna.


## Biblioteca Scikit-learning
Uma das principais na área de inteligência artificial, foi desenvolvida sobre os pacotes NumPy, SciPy e matpplotilib.


## Framework Luigi

Framework de execução criado pelo Spotfy que cria pipilines de dados em python


# Introdução ao Machine Learning
Treinar o sistema
Aprende com exemplos
Tomada de decisão com suporte de base de regras bem definidas, sem se basear na emoção

IA Geral - filmes, ficção científica

IA Restrita - sistemas para reconhecimento de face, compras, veículos autonomos, sensores de radar, cameras de vídeo, acelerômetros
	Aprendizado por reforço, com recompensas
	Redes neurais artificiais
	
	
Aprendizado de Máquina - treinamento, programar computadores para aprender um determinado comportamento ou padrão automaticamente a partir de exemplos ou observações, utilizando *datasets*

Teste de Turing - testa a capacidade de uma máquina exibir comportamento inteligente equivalente a um ser humano, ou indistinguível deste.

Robo Sophia
Primeiro robô a ter cidadania
Capaz de reproduzir 62 expressões faciais
Objetivo é conseguir uma maior aceitação da robótica no mesmo ambiente humano
Ainda não consegue passar no teste de Turing


TensorFlow - framework gratuito para machine learning


# Métodos de Machine Learning bioinspirados

Algoritmos bioinspirados
	* Inspirados no comportamehnto de seres vivos em convivencia social;
	* Conhecimento colaborativo compartilhado;
	* Métodos heurísticos (não determinísticos);
	* Buscam a melhor solução global;

	
# Redes Neurais Artificiais
Sinais de entrada
Pesos sinápticos
Combinador linear
Limiar de ativação
Sinal de saída(resposta)

Nossos olhos são sensores que capturam uma imagem por meio da visão e jogam a imagem para o cérebro;
Um treinamento é gerado por valores numéricos, pesos;














