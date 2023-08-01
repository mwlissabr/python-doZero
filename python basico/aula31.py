# Default : aquele que você define o valor no parâmetro
# Non-default : aquele que você não define valor no parâmetro 


def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque.')


boas_vindas('Marcos')

# Não pode alterar a ordem, caso você tenha um default e um non-default
# é necessário colocar o default por último