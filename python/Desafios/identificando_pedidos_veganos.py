numPedidos = int(input())


for i in range(1, numPedidos + 1):

  prato = input()

  calorias = int(input())

  ehVegano = input()

  vegano = ''

   
  if ehVegano == "s":

   vegano = "(Vegano)"

  else:

   vegano = "(Nao-vegano)"
    

  print(f'Pedido {i}: {prato} {vegano} - {calorias} calorias')