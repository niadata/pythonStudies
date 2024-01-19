Menu = '''
    teste

    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
    =>'''


saldo = 0
limite = 500
numeroSaque = 0
extrato = ""
limiteSaque = 3

while True:

    opcao = input(Menu)

    if opcao == "1":
        valor= float(input('digite o valor a ser depositado:'))
        if valor >0:
            saldo += valor
            extrato +=  f"Depósito: R$ {valor:.2f}\n"
            print('seu saldo atual é de', saldo )
            
        else:
            print('somente valores maior que zero')
    
    if opcao == "2":
        valor= float(input('digite o valor a ser sacado:'))
        
        if valor >0 and valor<=saldo:
            saldo -= valor
            extrato +=  f"Saque: R$ {valor:.2f}\n"
            numeroSaque =+ 1
            print("saque efetuado")
        
        if numeroSaque <= 3:
            print("Você atingiu  máxim de saques")
        
        else:
            valor= float(input("Valor invalido, por favor coloque um outro valor"))
    
    if opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    if opcao == "0":
        print("Você está fora do sistema")
        break     
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
            
