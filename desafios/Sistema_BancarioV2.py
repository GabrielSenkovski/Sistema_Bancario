import textwrap

def menu():
    menu = """

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Nova conta
        [5] Novo usuário
        [6] Ver Contas
        [q] Sair
        """ 
    return input(textwrap.dedent(menu))  


#função depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("operação efetuada com sucesso")
    else:
        print("Operação invalida!")

    return saldo, extrato

#função saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

#função extrato
def exibir_extrato (saldo, /, *, extrato):
    if not extrato:
        print ("Não foram realizadas movimentações nessa conta.")
    else:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================")

#função criar usuarios
def criar_usuario(usuarios):
    cpf = (input('informe os Números do seu CPF: '))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("(dd/mm/aaaa): ")
    endereco = input("(rua, numero, bairro, cidade , UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
      
    print("operação falhou, certifique-se se o preenchimento dos dados foi feito corretamente.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#chamador das funções
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        #opções abaixo:

        #deposito
        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        #saque
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar( saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        #extrato
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        
        elif opcao == "5":
            criar_usuario(usuarios )

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            listar_contas(contas)
       
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main()