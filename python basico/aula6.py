# Primeiro precisamos criar as variáveis
nome = 'André'
idade = 32
idade = str(idade)
cidade = 'São Paulo'

print('O ' + nome + ' tem ' + str(idade) + ' anos e mora na cidade de ' + cidade + '.')



# O André tem 32 anos de idade e mora na cidade de São Paulo.

'''
O código deu erro pois o sistema não consegue juntar dois tipos de dados diferentes (string e number)
em um print. A solução foi declarar que a variável de número era string, podendo também ser 
resolvido dentro mesmo do print, definindo que aquela variável no print se tornaria uma
string.
'''