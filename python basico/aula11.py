# Manipulando a string com métodos 

mensagem = 'eu adoro comida Caseira'

print(mensagem.lower())
print(mensagem.upper())
#Inicia a primeira palavra com letra maiúscula
print(mensagem.capitalize())
# Achando em qual posição do index está aquele caractere
print(mensagem.find('c'))
# Procurando por qual posiçao que inicia a palavra
print(mensagem.find('adoro'))
# O que quer encontrar e depois trocar todas iguais para a nova
print(mensagem.replace('a', 'e'))
print(mensagem.replace('Caseira', 'feita em casa'))
# Garantir que não existe espaços antes do primeiro caractere
print(mensagem.strip())
