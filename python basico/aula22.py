# Criando um 'retângulo' usando for loop

# 6x6
# simbolo = @

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas): # vai rodar 6x = outer loop
    for c in range(colunas): #vai rodar 6x = inner loop
        print(simbolo, end='') 
    print() # usando este print para que cada vez que a coluna seja finalizada, continue na próxima linha