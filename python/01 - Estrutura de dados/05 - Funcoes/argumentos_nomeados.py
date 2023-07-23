def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# nomeado
salvar_carro("Fiat", "Palio", 1999, "ABC-5546")
# chave:valor
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-5546")
# dicionario
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
