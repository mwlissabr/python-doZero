## == for loop nested ===

    # Outer loop
     # Inner loop


for numero1 in range(1,6):
    print('Produto ' + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)

# Modificarde FANTASTICO para F A N T A S T I C O 

palavra = 'FANTASTICO'

for space in palavra: # criei a variável space para indicar o espaço entre as letras, que eu chamei no print em seguida
    print(f' {space}' , end ='')

    # O print só funcionou com o espaço nas letras após dar um espaço entre o f' e {}
