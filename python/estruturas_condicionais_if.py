MAIOR_IDADE = 18
idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
if idade < MAIOR_IDADE:
    print("Menor de idade, ainda não pode tirar CNH.")
            