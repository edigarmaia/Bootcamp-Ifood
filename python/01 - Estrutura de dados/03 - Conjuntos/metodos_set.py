# union - união entre conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
conjunto_c = {4, 1, 2, 5, 6, 3 }
print(conjunto_a,conjunto_b.union(conjunto_b))

# intersection - a parte igual dos conjuntos
print(conjunto_a.intersection(conjunto_b))

# difference - a parte diferente dos conjuntos
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# symmetric difference - a parte que não está na intersecção
print(conjunto_a.symmetric_difference(conjunto_b))

# issubset - se todos os elementos de um conjunto estão no outro conjunto - boolean
print(conjunto_a.issubset(conjunto_c))
print(conjunto_c.issubset(conjunto_a))

# contrario do issubset
print(conjunto_a.issuperset(conjunto_c))
print(conjunto_c.issuperset(conjunto_a))

# isdisjoint - conjunto disjunto
conjunto_d = {1, 2, 3, 4, 5}
conjunto_e = {6, 7, 8, 9}
conjunto_f = {1,0}
print(conjunto_d.isdisjoint(conjunto_e))
print(conjunto_d.isdisjoint(conjunto_f))

# add - pode adicionar um elemento se ainda não existir
sorteio = {1,23}
print(sorteio)
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25)
print(sorteio)

# copy - fazer uma copia
sorteio2 = sorteio.copy()
print(sorteio2)

# discard - descarta um valor, se não existir, não vai dar erro
sorteio.discard(25)
print(sorteio)

# pop - remover valores da lista, sem precisar passar argumento
print(sorteio.pop())
print(sorteio)

# remove - remove um elemento que existe no conjunto, se não existir vai dar erro
sorteio.remove(42)
print(sorteio)

# clear - limpa o conjunto
sorteio.clear()
print(sorteio)

# len - pega o tamanho do conjunto
print(len(sorteio2))

# in - verifica se o objeto está dentro do conjunto
print(conjunto_a)
print(1 in conjunto_a)

print(conjunto_d)
print(5 in conjunto_d)