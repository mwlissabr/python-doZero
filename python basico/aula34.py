# Criar uma função que armazena números e strings (dados)


# Usando dois asteriscos para que indique que existe vários parâmetros
def agencia(**carro):
    return carro

# Definindo os parâmetros junto com os argumentos
print(agencia(Marca = 'Gol', Cor = 'Branco', Motor = 1.0, Placa = 1234))
print(agencia(Marca = 'Gol', Cor = 'Azul', Motor = 1.0))
print(agencia(Marca = 'Gol', Cor = 'Preto', Motor = 1.0, Placa = 1234))

