menu = """
=============== MENU ===============
[u] \tCriar Usuario
[c] \tCriar Conta
[d] \tDepositar
[s] \tSacar
[e] \tExtrato
[lu] \tListar Usuarios
[lc] \tListar Contas
[q] \tSair
====================================

=> """


def check_value(n):
    is_valid = False
    value = None
    try:
        value = float(n)
        is_valid = True
    except ValueError:
        pass

    return is_valid, value


def depositar(saldo, valor, extrato, /):
    is_valid, valor = check_value(valor)
    if is_valid:
        if valor <= 0:
            print("Operação não realizada. Valor inválido.")
        else:
            saldo += valor
            extrato += f"+ R$ {valor:.2f}\n"
            print("Operacao concluída.")
    else:
        print("Valor informado nao eh numérico.")

    return saldo, extrato


def sacar(
    saldo=0,
    valor=0,
    extrato=None,
    limite=500,
    numero_saques=0,
    limite_saques=3,
):
    is_valid, valor = check_value(valor)
    if is_valid:
        if numero_saques == limite_saques:
            print("Operacao nao realizada. Limite de 3 saques diarios.")
        else:
            if valor > limite:
                print(f"Operacao nao realizada. Limite de R$ {limite} por saque.")
            elif valor < 0:
                print("Valor informado eh invalido")
            elif saldo - valor < 0:
                print("Saldo insuficiente.")
            else:
                saldo -= valor
                extrato += f"- R$ {valor:.2f}\n"
                numero_saques += 1
                print("Operação concluida")
    return saldo, extrato


def exibir_extrato(saldo, /, extrato=""):
    print(f"Extrato\n\n{extrato}\nSALDO: {saldo:.2f}\n")


def criar_usuario(lista: list, nome, data_nascimento, cpf, endereco):
    usuario = {}
    usuario["nome"] = nome
    usuario["data_nascimento"] = data_nascimento
    usuario["cpf"] = cpf
    usuario["endereco"] = endereco

    found = False
    for cliente in lista:
        if cliente.get("cpf") == cpf:
            found = True
            break

    if not found:
        lista.append(usuario)
    else:
        print("Ja ha cliente com o CPF informado cadastrado")


def exibir_lista(lista: list):
    for usuario in lista:
        print(usuario, end="\n")


def criar_conta(lista_contas: list, lista_clientes: list, cpf_usuario):
    conta = {}
    conta["agencia"] = "0001"
    conta["nro_conta"] = (
        int(lista_contas[-1].get("nro_conta")) + 1 if lista_contas else 1
    )
    conta["cpf_usuario"] = cpf_usuario

    found = False
    for cliente in lista_clientes:
        if cliente.get("cpf") == cpf_usuario:
            found = True
            break

    if found:
        lista_contas.append(conta)
    else:
        print("Usuario nao cadastrado")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    on_loop = True
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []
    while on_loop:
        opcao = input(menu)

        if opcao == "d":
            print("Operacao de Deposito foi selecionada.")
            deposito = input("Valor a depositar: ")
            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "s":
            print("Operacao de Saque foi selecionada.")
            saque = input("Informe um valor: ")
            saldo, extrato = sacar(
                saldo=saldo,
                valor=saque,
                extrato=extrato,
                limite=500,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            nome = input("Informe nome: ")
            data_nascimento = input("Informe data de nascimento: ")
            cpf = input("Informe cpf: ")
            endereco = input("Informe endereco: ")
            criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

        elif opcao == "lu":
            exibir_lista(usuarios)

        elif opcao == "c":
            cpf = input("Informe cpf do usuario: ")
            criar_conta(contas, usuarios, cpf)

        elif opcao == "lc":
            exibir_lista(contas)
        else:
            on_loop = False


if __name__ == "__main__":
    main()
