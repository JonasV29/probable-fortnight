#nesse código ele calcula os juros composto

valor_inicial = 5000
taxa_juros = 0.08
periodo = 5

valor_final = valor_inicial * (1 + taxa_juros)** periodo #a fórmula do juros composto

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.

print("Valor final do investimento: R$ {:.2f}" .format(valor_final))