# Funções

Bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses podem ou não ter valores padrões.
torna o código mais legível e possibilita o reaproveitamento de código.
Programação de maneira estruturada.

def - indica que temos uma função

def indicador():

## Retornando valores

Utilizamos a palavra reservada return.
Toda função retorna None por padrão
Uma função pode retornar mais de um valor

## Argumentos nomeados

Funções também podem ser chamadas usando argumentos nomeados da forma chave:valor.

## Args e kwargs

Podemos combinar parametros obrigatórios com args e kwargs.
Quando esses são definidos (\*args e \*\*kwargs), o método recebe os valores como tupla e dicionario respectivamente.

## Parametros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome.
Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

## Objetos de primeira classe

Em Python tudo é objeto, dessa forma funções tambem são objetos, o que as tornam objetos de primeira classe.
Com isso podemos atribuir funções a variáveis, passá-las como parametro para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionarios etc) e usar como valor de retorno para uma função(closures).

## Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco da função o escopo é local. Portanto alterações ali feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado.
Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
Essa NÃO É UMA BOA PRATICA E DEVE SER EVITADA.
