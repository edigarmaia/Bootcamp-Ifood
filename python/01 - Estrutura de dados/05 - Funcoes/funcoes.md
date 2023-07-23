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