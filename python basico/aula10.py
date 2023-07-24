#Aprendendo a utilizar o Formated Strings (f'')

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

# Primeira forma de imprimir a frase, usando uma variável de texto
texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + ']'

print(texto)

# Segunda forma, utilizando a string formatada
texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'

print(texto2)


# O Marcos Silva é um excelente [Programador]