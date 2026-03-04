saldo = 1000

while True:  # loop infinito (vai rodar até mandar parar)

    print("\nMENU")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        deposito = float(input("Quanto você deseja depositar? "))
        saldo += deposito
        print(f"Deposito efetuado! Saldo atual de {saldo} reais")

    elif opcao == "2":
        saque = float(input("Quanto você deseja sacar? "))
        if (saque > saldo):
            print(f"Erro! Saque maior que seu saldo. Saldo atual de {saldo} reais")
        else:
            saldo -= saque
            print(f"Saque efetuado! Saldo atual de {saldo} reais")

    elif opcao == "3":
        print("Encerrando o programa...")
        break  # sai do while

    else:
        print("Opção inválida! Tente novamente.")