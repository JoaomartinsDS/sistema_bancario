conta_saldo = 0
saque_feito = 0
saque_limite = 3
saque_maximo = 500
extrato = ""
exibir_menu = True
while exibir_menu == True:
    print("""          ### MENU ###
      Selecione uma opçã0:
      (d) depósito
      (s) saque
      (e) extrato
      (x) sair""")

    opcao = input()
    if opcao == 'd':
        valor_deposito = float(input("Digite o valor de depósito: "))
        if valor_deposito > 0:
            conta_saldo += valor_deposito
            valor_deposito = f"R$ {valor_deposito:.2f}"
            extrato += f"\ndeposito: {valor_deposito}"
        else:
            print("depósito precisa ser de pelo menos 1 real.")
    elif opcao == 's':
        if saque_feito < saque_limite:
            saque_user = float(input("Digite o valor de saque: "))
            if saque_user <= saque_maximo:
                if saque_user <= conta_saldo:
                    conta_saldo -= saque_user
                    saque_feito += 1
                    saque_user = f"R${saque_user:.2f}"
                    extrato += f"\nsaque: {saque_user}"
                    
                else:
                    print("saldo insuficiente para o saque")
            else:
                print("Só pode sacar valores até R$ 500,00")
        else:
            print("Você não pode realizar mais de 3 saques no dias")
    elif opcao == "e":
        if extrato == []:
            
            print(""" 
                ############### EXTRATO ################
                Não foi realizado nenhuma movimentação""")
        else:
            print("========== EXTRATO ==========")
            print(extrato)
            print(f"\nSaldo: R$ {conta_saldo:.2f}")

            print("====================")
    elif opcao == "x":
        print("Obrigado por utilizar nosso banco")
        break
                


            