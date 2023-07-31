# if else é sempre com uma condição, verdadeiro ou falso

# for loop é um loop para utilizar quando você sabe o 'fim' do loop

# while loop é um loop que se utiliza quando não sabemos o tamanho do loop, 
# enquanto a condição for verdadeira

print('Utilizando If e Else para ver se a primeira condição é verdadeira')
if 10 >= 5:
    print('Verdadeiro!')
else:
    print('Falso!')


print('Utilizando for para imprimir a contagem de 1 até 10')
for condicao1 in range(1,11):
    print(f'{condicao1} ', end='')
print() # tive que colocar um print no final pois ele não estava quebrando 
# a linha sozinho


numero1 = 1

print('Utilizando o while para imprimir até 10 enquanto o número for menor que 10')
while numero1 <= 10:
    print(numero1)
    numero1 += 1