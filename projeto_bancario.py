#  Comentário

menu = "[d] Depositar\n[s] Sacar\n[e] Extrato\n[q] Sair: "

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("")
    opcao = input(menu)
    if opcao == 'd':
        print("")
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0:
             saldo += deposito
             print("")
             print("Depósito efetuado com sucesso.")
             print(f"Saldo atual: R${saldo}")
        else:
            print("")
            print("Valor de saque inválido, tente novamente.")
        extrato += f'+ R${deposito} \n'
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            print("")
            saque = float(input("Digite o valor para o saque: "))
            if saque > saldo:
                print("")
                print("Saldo insuficiente.")
                print(f"Saldo atual: R${saldo}")
            elif saque > limite:
                print("")
                print("Saque máximo de R$500,00.")
            else: 
                saldo -= saque
                numero_saques += 1
                print("")
                print("Saque efetuado com sucesso.")
                print(f"Saldo atual: R${saldo}")
                extrato += f'- R${saque} \n'
        else:
            print("")
            print("Limite de saques diários atingido.")
    elif opcao == 'e':
        print("")
        print("EXTRATO:")
        print(extrato)
    elif opcao == 'q':
        print("Programa encerrado.")
        break
    else: 
        print("Operação inválida, por favor selecione novamente a opção desejada.")
