# criando um dicionario
pessoa = {"nome": "Edigar", "idade": 40}
print(pessoa)

# usando a classe dict()
pessoa = dict(nome="Edigar", idade=40)
print(pessoa)

# adicionando ao dicionario
pessoa["telefone"] = "1234-5789"
print(pessoa)

# acessando valores
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

# subescrevendo valores
pessoa["nome"] = "Maria"
pessoa["idade"] = 25
pessoa["telefone"] = "9972-1234"

print(pessoa)