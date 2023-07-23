def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anonimo"):
    print(f"Seja bem {nome}!")

exibir_mensagem()
exibir_mensagem2(nome="Maria")
exibir_mensagem3("Aninha")
exibir_mensagem3(nome="Ana")