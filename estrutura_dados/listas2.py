numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

# imprimindo a lista várias vezes
final = numeros * 2

# concatenando as listas
final2 = numeros + letras
print(final, final2)

# utilizando extend para concatenar as listas
numeros.extend(letras)
print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]

# puxando um item específico dentro do index
print(itens[0][1])