valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

total_hamburgueres = valorHamburguer * quantidadeHamburguer
total_bebida = valorBebida * quantidadeBebida
preco_final_pedido = total_hamburgueres + total_bebida
troco_pedido = valorPago - preco_final_pedido

print(f"O preço final do pedido é R$ {preco_final_pedido:.2f}. Seu troco é R$ {troco_pedido:.2f}.")
