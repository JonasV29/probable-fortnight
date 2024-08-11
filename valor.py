saldo_total = 300
valor_saque = 200
saldo_atual = 0

if saldo_total > valor_saque:
  saldo_atual = saldo_total - valor_saque
  print("Saque realizado com sucesso. Novo saldo:  ", saldo_atual)
else:
  print("Saldo insuficiente. Saque nao realizado!")
# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.