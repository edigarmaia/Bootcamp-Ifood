carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# com enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")