
menu = [ "1-Sacar", "2-Depositar","3-Extrato","4-Sair:"]


saldo = 0   # Declarando as variáveis 
limite = 500 # No programa vai ter um limite de saque de 500 e vai poder sacar 3 vezes
extrato = ""
numero_saque = 0
limite_saque = 3

while True:   # Vai ser loop para a pessoar escolher as opções como se fosse mesmo um banco
              # Porém se a pessoa escolher o número 4 o loop vai ser quebrado e o programa vai ser finalizado
        
        opcao = int(input(menu))

        if opcao == 1:
                valor = float(input("Qual valor você vai querer sacar: "))
                
                # Aqui vai o cálculo se a pessoa exigiu o limite de saldo,saque ou se digitou um valor incorreto
                
                excedeu_saldo = valor > saldo

                excedeu_limite = valor > limite 

                excedeu_saques = numero_saque >= limite_saque

                if excedeu_saldo:
                        print("Infelizmente, você não saldo suficiente!")

                elif excedeu_limite:
                        print("Você passou do limite de saque") 

                elif excedeu_saques:
                        print("O número máximo de saques foi exedido.")

                elif valor > 0:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        numero_saque += 1

                else:
                        print("Operação falhou, por que o valor digitado é incorreto.")

        elif opcao == 2:
               valor = float(input("Qual valor você vai querer depositar: "))
               
               if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
               else:
                print("Operação falhou, o valor inserido está incorreto!")

               
        elif opcao == 3:
                print("\n************ EXTRATO ************")
                print("Não foram realizadas alterações" if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("**********************************")
        elif opcao == 4:
                break
        else:
                print("Opção inválida,por favor selecione a opção válida.")
        
        
      
        


