contatos = {
"edigarmaia@gmail.com": {"nome": "Edigar", "telefone": "95249-7242"}
}
# clear - limpa o dicionario
print(contatos)
contatos.clear()
print(contatos)

contatos = {
"edigarmaia@gmail.com": {"nome": "Edigar", "telefone": "95249-7242"}
}
# copy faz uma copia do dicionario
copia = contatos.copy()
print(copia)

# fromkeys - cria chaves sem valor
dict.fromkeys(["e-mail", "celular"])

# get - acessa valores no dicionario
print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("edigarmaia@gmail.com", {}))

# items - retorna uma lista de tuplas
print(contatos.items())

# keys - retorna as chaves do dicionario
print(contatos.keys())

# pop - remove e retorna o valor removido
resultado = contatos.pop("edigarmaia@gmail", {})
print(resultado)
print()
# popitem - remove itens na sequencia sem precisar passar a chave
resultado = contatos.popitem()
print(resultado)

# setdefault
contatos.setdefault("nome", "Maria")
print(contatos)

print()
# update - permite atualizar o dicionario com outro dicionario
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
print()

# values - retorna os valores do dicionario
resultado = contatos.values()
print(resultado)
print()

# in - verifica se existe ou não uma chave no dicionario
resultado = "guilherme@gmail.com" in contatos
print(resultado)
print()
resultado = "idade" in contatos ["guilherme@gmail.com"]
print(resultado)

# del - remover um objeto
del contatos["guilherme@gmail.com"]["telefone"]
print(contatos)