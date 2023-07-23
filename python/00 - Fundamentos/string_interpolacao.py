nome  = "Edigar"
idade = 40
linguagem = "Python"
saldo = 45.125

# usando dicionario
dados = {"nome": "Edigar Maia", "idade": 40}
print("Nome: %s Idade: %s Linguagem: %s" % (nome, idade, linguagem))

print("Nome: {} Idade: {} Linguagem: {}".format(nome, idade,linguagem))

print("Nome: {0} Idade: {1} Linguagem: {2}".format(nome, idade,linguagem))

print("Nome: {nome} Idade: {idade} Linguagem: {linguagem}".format(nome=nome, idade=idade,linguagem=linguagem))

print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: R$ {saldo:5.2f}")


print(f"Nome: {nome} Idade: {idade} Saldo: R$ {saldo:.2f}")