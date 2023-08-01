# Funções fazem basicamente duas coisas: realiza uma tarefa ou retorna um valor


# Isso pe um exemplo de tarefa, pois ela imprimiu na tela o que foi pedido
# sem armazenar nada
def cliente1(nome):
    print(f'Olá {nome}')


# Aqui ele vai armazenar o valor, pois está retornando e não ó imprimindo
def cliente2(nome):
    return f'Olá {nome}'


x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)