def main(): 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    AGENCIA = 2000
    limite_saques = 3
    verificador = True
    while verificador:
        print("""@@@@@@ MENU @@@@@@ """)
        print("(d) - Deposito")
        print("(s) - Saque")
        print("(e) - Extrato")
        print("(x) - Sair")
        print("(nu) - Cadastrar usuário")
        print("(nc) - nova conta")
        print("(lc) - listar contas")
        opcao = input("Digite a opção desejada: ")
        if opcao == "d":
            valor = int(input("Digite o valor de depósito: "))
            saldo,extrato = deposito(saldo, valor,extrato)
        if opcao == "s":
            valor = int(input("Digite o valor a ser sacado: "))
            
            saldo,extrato = saque(saldo = saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
        if opcao == "e":
            exibir_extrato(saldo,extrato)
        if opcao == "nu":
            criar_usuario(usuarios)
        if opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        if opcao == "lc":

            for conta in contas:
                print("========================================================")
                print(f""" 
                Agência:\t{conta['agencia']}
                Conta:\t\t{conta["numero_conta"]}
                Titular:\t{conta["usuario"]["nome"]}""")
            








def deposito(saldo,valor,extrato, / ):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: \tR$ {valor:.2f}"
        print("f(valor depositado com sucesso!)")
    else:
        print("Falha ao depositar. Valor de depósito inválido.")
    return saldo,extrato

def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_saques = numero_saques > limite_saques
    excedeu_limite = valor > limite
    if excedeu_saldo:
        print("Operação falhou. Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("O valor de saque excede o limite.")
    elif excedeu_limite_saques:
        print("Você atingiu o limite de saque diário.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\nSaque: \t\t R${valor:.2f}"
        print("Saque realizado com sucesso!")
    else:
        print("Erro. valor de saque inválido.")
    return saldo,extrato

def exibir_extrato(saldo,extrato):
    print("""@@@@@@ EXTRATO @@@@@@ """)
    if extrato == "":
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"\nsaldo atual: \t {saldo:.2f}")
def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o cpf: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Usuário já cadastrado")
        return
    nome=input("digite o nome: ")
    data_nascimento=input("Digite a data de nascimento: ")
    endereco = input("Digite o seu endereço: ")
    usuarios.append({"cpf":cpf,"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco})
    print("usuario cadastrado com sucesso")
def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {'agencia': agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("Usuário não cadastrado. Encerrando fluxo de criação de conta.")


main()
    





            