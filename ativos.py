ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input("Qual a quantidade de ativos?"))

# Entrada dos códigos dos ativos
for x in range(quantidadeAtivos):
    codigoAtivo = input("Coloque seus códigos ativos: ")
    ativos.append(codigoAtivo)
    
    
#aqui faz com que entre em ordem alfabética   
ativos.sort()

#eu coloquei com espaço e esse código é para funcinar só com 3 elementos
print(ativos[0], "\n", ativos[1], "\n", ativos[2])