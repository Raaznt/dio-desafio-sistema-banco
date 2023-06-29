def check_value(n):
    is_valid = False
    value = None
    try:
        value = float(n)
        is_valid = True
    except ValueError:
        pass

    return is_valid, value


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
on_loop = True
LIMITE_SAQUES = 3

while on_loop:
    opcao = input(menu)

    if opcao == "d":
        print("Operacao de Deposito foi selecionada.")
        deposito = input("Valor a depositar: ")
        is_valid, deposito = check_value(deposito)
        if is_valid:
            if deposito <= 0:
                print("Operação não realizada. Valor inválido.")
            else:
                saldo += deposito
                extrato += f"+ R$ {deposito:.2f}\n"
                print("Operacao concluída.")
        else:
            print("Valor informado nao eh numérico.")

    elif opcao == "s":
        print("Operacao de Saque foi selecionada.")
        saque = input("Informe um valor: ")
        is_valid, saque = check_value(saque)
        if is_valid:
            if numero_saques == LIMITE_SAQUES:
                print("Operacao nao realizada. Limite de 3 saques diarios.")
            else:
                if saque > 500.00:
                    print("Operacao nao realizada. Limite de R$ 500.00 por saque.")
                elif saque < 0:
                    print("Valor informado eh invalido")
                elif saldo - saque < 0:
                    print("Saldo insuficiente.")
                else:
                    saldo -= saque
                    extrato += f"- R$ {saque:.2f}\n"
                    numero_saques += 1
                    print("Operação concluida")

    elif opcao == "e":
        print(f"Extrato\n\n{extrato}\nSALDO: {saldo:.2f}\n")

    else:
        on_loop = False
