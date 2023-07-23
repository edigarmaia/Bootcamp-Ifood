lista = []

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

#print (lista)

# limpando a lista
#lista.clear()
print (lista)

# copiando a lista
l2 = lista.copy()
print(l2)

# mostrando id das listas
print(id(l2), id(lista))

# adicionando um objeto em l2
l2.append(5)
print(l2)

# count - quantas vezes determinado objeto aparece na lista
cores = ["vermelho", "amarelo", "azul"]

print(cores.count("vermelho"))
print(cores.count("amarelo"))
print(cores.count("azul"))

# extend - juntar duas listas
linguagens = ["Python", "Java", "JavaScript", "Ruby", "Lua"]
print(linguagens)

linguagens.extend(["C", "C#", "TypeScript", "PHP"])
print(linguagens)

# index - pega a primeira ocorrencia do objeto
print(linguagens.index("JavaScript"))

# pop - retira um elemento do topo da lista, o último que foi adicionado
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

# remove - retira um objeto da lista
linguagens.remove("C")
print(linguagens)

# reverse - faz um espelhamento da lista
linguagens.reverse()
print(linguagens)

# sort - ordena a lista
linguagens.sort() #ordem alfabetica
print(linguagens)

linguagens.sort(reverse=True) #ordem reversa
print(linguagens)

linguagens.sort(key=lambda x: len(x)) #ordem por tamanho da palavra, do menor para o maior
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True) #ordem por tamanho da palavra, do maior para o menor
print(linguagens)

# len - pega o tamanho da lista
print(len(linguagens))

# sorted - uma função que ordena listas, similar ao sort
sorted(linguagens, key=lambda x: len(x))
#sorted(linguagens, key=lambda x: len(x), reverse=True)
print(sorted(linguagens))