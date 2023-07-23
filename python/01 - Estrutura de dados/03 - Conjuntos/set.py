letras = set("abacaxi")
print(letras)
print()

carros = set(("palio", "gol", "celta", "palio"))
print(carros)
print()
# iterando
for carro in carros:
    print(carro)

print()

# iterando com indice
for carro in enumerate(carros):
    print(carro)

print()

linguagens = {"python", "java", "python"}
print(linguagens)

print()
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)
# acessando os valores do conjunto
numeros = list(numeros)
print(numeros[0])

