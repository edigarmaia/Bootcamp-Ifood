# Python

Nasceu em 1989 como um hobby, do programador Guido Van Rossum, a ideia era dar continuidade a linguagem ABC, que era desenvolvida no Centro de Pesquisa Holandês (CWI).

- fácil e intuitiva
- código aberto, para que todos possam contribuir
- código tão inteligível quanto inglês
- adequada para tarefas diárias e produtiva

Em 2001 nasce o Python 2.1 a documentação e especificação da linguagem

Em 2008 nasce a versão 3.0 que resolveu problemas de design da linguagem e melhorou a performance.

Versão atual 3.10.2

Linguagem muito versátil

- tipagem dinâmica e forte
- multiplataforma e multiparadigma
- comunidade gigante e ativa
- curva de aprendizado baixa

---

## Tipos de dados

Definem as caracteristicas e comportamentos de um valor (objeto) para o interpretador e quanto de espaço vai ocupar na memoria

texto -> str
numerico -> int, float, complex
sequencia -> list, tuple, range
mapa -> dict
colecao -> set, fronzenset
booleano -> bool
binario -> bytes, bytearray, memoryview

---

int -> numeros inteiros
float -> numeros com pontos flutuantes
bool -> True or False
str -> valores alfanuméricos

---

Modo interativo, escrever o codigo e já ver em tempo real
Para entrar: digite no terminal, python ou python3 e enter
Para sair: exit()

Funcões
dir() -> retorna a lista de nomes no escopo local atual
dir(100)

help() -> sistema de ajuda integrado, é possível fazer buscas em modo interativo ou informar por parametro qual o nome do módulo, função, classe, método ou variavel.
help(100)

---

Variaveis
Não precisamos definir o tipo da variavel, o python identifica automaticamente.

Constantes
Uma constante nasce com um valor e permanece com ele até o final do programa.
Em python não temos constantes, para usar uma variavel como constante devemos criar com o nome todo em letras maiusculas

---

Boas práticas
Padrão de nomes em snakeCase
Escolher nomes sugestivos
Nome de constante todo em maiusculo

---

Função entrada
input - lê como string

Função saída
print

---

## Operadores aritméticos

- soma

* subtração

- multiplicação
  / divisão - retorna um float
  // divisão inteira - retorna um inteiro
  % mod - resto da divisão
  \*\* exponenciação

Precedencia dos operadores
1º Parentêsis
2º Expoentes
3º Multiplicação e divisão, da esquerda para a direita
4º Somas e subtrações, da esquerda para a direita

## Operadores de comparação

== igual
!= diferente
. > maior
. >= maior ou igual
< menor
<= menor ou igual

## Operadores de atribuição

= atribuição
+= atribuição com adicao

## Operadores lógicos

and - V se as duas condições são V
or - V se ao menos uma condição for V
not - retorna Falso se o resultado for verdadeiro

## Operadores de identidade

is - compara se dois obejtos ocupam a mesma região de memória
is not - compara se dois obejtos não ocupam a mesma região de memória

## Operadores de associação

Verifica se um objeto está presente em uma sequencia
in - not in

## Indentação e blocos

Identar é uma forma de manter o código mais legível e mais manutenível
Atraves da indentação o interpretador consegue determinar onde um bloco inicia e onde termina

Por convenção a cada nova linha utiliza quatro espaços para identar e definir os blocos

## Estruturas condicionais

Permitem o desvio do fluxo de controle, quando determinadas expressões lógicas são atendidas

## Estruturas de repeticao

Repete um determinado código por um numero de vezes, esse numero pode ser conhecido ou determinado atraves de uma expressao logica

- For - mais indicado quando sabemos o número exato de vezes que o bloco de código deve ser executado ou quando queremos percorrer um objeto iterável.

- While - faz sentido usar quando nao sabemos o número exato de vezes que o bloco de código deve ser executado.

## Strings e fatiamento

### Interpolação de variaveis

F-String
print(f"valor de PI: {PI:.2f}")# definindo duas casas decimais
