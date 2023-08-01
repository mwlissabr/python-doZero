# Listas
    # armazenar mais de uma informaçõa em variáveis
    # manter a sequência dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'


# utilizando o [] em uma variável para inserir mais dados
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiânia']
#                0                1            2           3
numeros = [2, 4, 6]
#          0  1  2

# print(cidades)
# puxando um valor específico do index
# print(cidades[1])
# print(cidades[-1])
# print(numeros)

# trocando o valor
cidades[0] = 'Brasília'

# Adicionando um item no final da lista usando uma função pronta
cidades.append('Santa Catarina')

# Removendo um item
cidades.remove('Salvador')

# Adicionando um item numa posição específica do index
cidades.insert(1, 'Bahia')

# Removendo um item através da posição do index
cidades.pop(0)

# Organizar em ordem alfabética
cidades.sort()
print(cidades)