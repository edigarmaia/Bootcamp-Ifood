# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
        #retorno   iteração           condição
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#versao 2
pares2 = []
for numero in numeros:
    if numero % 2 == 0:
        pares2.append(numero)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)