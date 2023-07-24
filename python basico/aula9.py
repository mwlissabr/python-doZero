# Como usar o slice

fruta = 'abacate'
#index   0123456

# Cada caractere da variável ocupa um espaço no index 
print(fruta[3])
# Aqui ele imprimiu apenas o espaço do index solicitado, nesse caso o espaço 3 da letra 'c'

print(fruta[2:5])
# Usando o index puxando de um caractere até o outro em sequência

valor = str(99.75)
#index  01234

print(valor[3:5])

'''
Slice é pegar 'porções do seu string e trabalhar com ela de forma isolada'
'''