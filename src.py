saldo = 0
limite= 0
extrato = 0


LIMITE_DIARIO = 500
LIMITE_SAQUES = 3
historico_deposito = []
historico_saque = []

menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)
    opcao = opcao.strip().lower()
    
    if opcao == "d":
        try:
            valor = float(input("Informe o valor do deposito: "))
        except ValueError:
            print("Valor inválido")
            continue
        if valor <= 0:
            print("Valor inválido")
            continue
        saldo += valor
        print(f"Deposito de R${valor:.2f} efetuado com sucesso.")
        historico_deposito.append(valor)
        continue
    if opcao == "s":
        if len(historico_saque) >= LIMITE_SAQUES:
            print("Limite de saques atingido")
            continue
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError: 
            print("Valor inválido")
            continue
        if valor <= 0:
            print("Valor inválido")
            continue
        if valor > LIMITE_DIARIO:
            print("Limite de saque atingido, saque nao efetuado")
            continue
        if valor > saldo:
            print("Saldo insuficiente")
            continue
        saldo -= valor
        print(f"Saque de R${valor:.2f} efetuado com sucesso.")
        historico_saque.append(valor)
        continue
    if opcao == "e":
        print("Extrato:\n")

        print("\nHistórico de depositos:")
        for i in [f"Deposito de R${deposito:.2f}" for deposito in historico_deposito]:
            print(f'\n      {i}')
        print('\nHistórico de Saques:')
        for i in [f"Saque de R${saque:.2f}" for saque in historico_saque]:
            print(f'\n      {i}')
        print(f"\nSaldo: R${saldo:.2f}")

        continue
        
    if opcao == "q":
        break
    else:
        print("Opção inválida")
        continue
