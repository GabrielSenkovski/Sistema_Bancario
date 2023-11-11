import textwrap

def show_menu():
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


def deposit(saldo, value, statement, /):
    if value > 0:
        saldo += value
        statement += f"Depósito:\tR$ {value:.2f}\n"
        print("Operação concluída com sucesso")
    else:
        print("Operação inválida!")

    return saldo, statement


def withdraw(*, saldo, value, statement, limit, num_withdrawals, withdrawal_limit):
    exceeded_balance = value > saldo
    exceeded_limit = value > limit
    exceeded_withdrawals = num_withdrawals >= withdrawal_limit
    
    if exceeded_balance:
        print("Operação falhou! Saldo insuficiente.")

    elif exceeded_limit:
        print("Operação falhou! Valor do saque excede o limite.")

    elif exceeded_withdrawals:
        print("Operação falhou! Número máximo de saques atingido.")

    elif value > 0:
        saldo -= value
        statement += f"Saque: R$ {value:.2f}\n"
        num_withdrawals += 1

    else:
        print("Operação falhou! Valor informado é inválido.")

    return saldo, statement


def display_statement(saldo, /, *, statement):
    if not statement:
        print("Não há movimentações nesta conta.")
    else:
        print("\n================ EXTRATO ================")
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================")


def create_user(users):
    cpf = input('Informe os números do seu CPF: ')
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ Usuário com CPF já existe! @@@")
        return
    
    name = input("Informe o nome completo: ")
    birth_date = input("(dd/mm/aaaa): ")
    address = input("(Rua, número, bairro, cidade, UF): ")

    users.append({"nome": name, "data_nascimento": birth_date, "cpf": cpf, "endereco": address})

    print("Usuário criado")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def create_account(agency, account_number, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filter_user(cpf, users)

    if user:
        print("Conta criada!")
        return {"agencia": agency, "numero_conta": account_number, "usuario": user}
      
    print("Operação falhou. Verifique se os dados foram preenchidos corretamente.")


def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agência:\t{account['agencia']}
            C/C:\t\t{account['numero_conta']}
            Titular:\t{account['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    saldo = 0
    limit = 500
    statement = ""
    num_withdrawals = 0
    users = []
    accounts = []

    while True:
        option = show_menu()

        if option == "1":
            value = float(input("Informe o valor do depósito: "))
            saldo, statement = deposit(saldo, value, statement)

        elif option == "2":
            value = float(input("Informe o valor do saque: "))
            saldo, statement = withdraw(saldo=saldo,
                                        value=value,
                                        statement=statement,
                                        limit=limit,
                                        num_withdrawals=num_withdrawals,
                                        withdrawal_limit=WITHDRAWAL_LIMIT)

        elif option == "3":
            display_statement(saldo, statement=statement)

        elif option == "5":
            create_user(users)

        elif option == "4":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)
        
        elif option == "6":
            list_accounts(accounts)
       
        elif option == "q":
            break

        else:
            print("Operação inválida. Por favor, selecione novamente.")
main()