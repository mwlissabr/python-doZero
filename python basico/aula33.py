# X args = posso adicionar vários arugumentos

# Criar uma função que soma vários números

# usando o * para definir que podem ter várias entradas
def soma(*numeros):
    # definindo um ponto de partida para o loop
    resultado = 0
    # criando uma variável num quee vai conter o valor de numeros, separadamente
    for num in numeros:
    # somando o resultado que definimos o ponto de partida antes, com o número inserido
        resultado += num
    # pedindo para o return armazenar essa soma
    return resultado
    

# criando uma variável para a função
x = soma(2, 3, 4, 7)

# imprimindo a variável que contém a função
print(x)


# Testando com multiplicação
def multiplicar(*numeros2):
    resultado = 1
    for num in numeros2:
        resultado *= num
    return resultado


y = multiplicar(2, 4, 5)

print(y)
