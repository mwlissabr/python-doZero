# def boas_vindas_Marcos():
#     print('Olá Marcos!')
#     print('Temos 5 laptops em estoque.')
    

# def boas_vindas_Ronaldo():
#     print('Olá Ronaldo!')
#     print('Temos 4 laptops em estoque.')


# def boas_vindas_Linda():
#     print('Olá Linda!')
#     print('Temos 2 laptops em estoque.')


# boas_vindas_Marcos()
# boas_vindas_Ronaldo()
# boas_vindas_Linda()


# Fazendo com que 3 funções se torne uma só
# Dentro dos () vai o PARAMETRO

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')

# Ao chamar a função, dentro dos () vai o ARGUMENTO
boas_vindas('Marcos', 5)
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2)