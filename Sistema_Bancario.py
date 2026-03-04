menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: \n"))
        if valor > 0:
            saldo = valor + saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print(f"o {valor} é invalido para está operação!")
    
    elif opcao == "2":
        if numero_saques != LIMITE_SAQUES:
            
            retirado = float(input("Quando você deseja retirar? (MÁXIMO R$500.00) \n"))
            if retirado > limite:
                print("numero maior que R$500,00")
            
            elif retirado > saldo:
                print("você não tem esse dinheiro na conta!")

            elif retirado > 0:
                saldo -= retirado
                numero_saques += 1 
                extrato += f"Saque: R$ {retirado:.2f}\n"
                print("Saque realizado com sucesso!")
        
        else:
            print("você atingiu o limite de saques diários!")
    
    elif opcao =="3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao=="4":
        print("fim da operação!")
        break
    
    else:
        print("você não digitou nenhuma das opções!")
    

