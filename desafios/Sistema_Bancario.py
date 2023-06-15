menu = """  OPERAÇÕES
                        [1] - Depositar
                        [2] - Sacar
                        [3] - Extrato
                        [4] - Sair
Digite a operação desejada abaixo:
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao  = input(menu)

    if opcao == "1":
        valor = float(input(" valor do depósito: "))

        if valor > 0:
            print(f"Deposito realizado com sucesso! R$ {valor:.2f}\n")
            saldo += valor
            extrato += f"Depósito realizado: {valor:.2f}\n"

        else:
            print("O valor informado é inválido")
    
    elif opcao == "2":
        
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O numero maximo de saques atingido.")

        elif valor > 0:
            print(f"Saque reaizado com sucesso! R$ {valor:.2f}\n")
            saldo -= valor
            extrato += f"Saque realizado: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou: O valor informado é inválido.")

        

    elif opcao == "3":
        print("============================== EXTRATO ==============================")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================================")

    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, porfavor selecione um comando válido.")