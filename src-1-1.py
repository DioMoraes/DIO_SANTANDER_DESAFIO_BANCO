
import textwrap
def menu():
    menu = """
    [d] Deposito
    [s] Saque
    [e] Extrato
    [c] Criar Conta
    [u] Criar Usuario
    [l] Listar Contas
    [q] Sair


    => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, LIMITE_SAQUES, numero_saques, LIMITE_VALOR_SAQUE = 500):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques atingido")
        return saldo, extrato
    else:
        if valor > saldo:
            print("Saldo insuficiente")
            return saldo, extrato
        if valor > LIMITE_VALOR_SAQUE:
            print("Limite diario de valor de saque atingido")
            return saldo, extrato
        else:
            saldo -= valor
            extrato += f"\nSaque de R${valor:.2f}\n"
            print(f'Saque de R${valor:.2f} efetuado com sucesso.')
            return saldo, extrato
    

    
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDeposito de R${valor:.2f}\n"
        print(f'Deposito de R${valor:.2f} efetuado com sucesso.')
    else:
        print("Valor inválido")

    return saldo, extrato

def exibe_extrato(saldo,/,*, extrato):
    print("Extrato:\n")
    if not extrato:
        print("Nao foram realizadas movimentacoes")
    else:
        print(extrato)
    print(f"Saldo: R${saldo:.2f}")


    

def criar_usuario(usuarios):
    """sem usuarios repetido"""
    
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print(f'Usuario {usuario["nome"]} já cadastrado')
        return
    nome = input('Informe o nome completo:')
    data_nascimento = input('Informe a data de nascimento:')
    endereco = input('Informe o endereço no formato: logadouro, numero, bairro, cidade/sigla estado:')
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})   
    
    
    
    
def filtrar_usuario(cpf, usuarios):
    usuario_exsite = [usuarios for usuarios in usuarios if usuarios["cpf"] == cpf]
    return usuario_exsite[0] if usuario_exsite else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario nao encontrado, fluxo de criacao de conta encerrado")
    return None
    
    
def listar_contas(contas):
    if not contas:
        print("Contas nao encontradas")
        return None
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    
    
def main():
    contas = []
    AGENCIA = '0001'
    LIMITE_DIARIO = 500
    LIMITE_SAQUES = 3
    saldo = 0
    extrato = ''
    historico_saque = []
    usuarios = []
    
    
    
    while True:
        opcao = menu()

        
        if opcao == "d":
            try:
                valor = float(input("Informe o valor do deposito: "))
            except ValueError:
                print("Valor inválido")
                continue
            
            saldo, extrato = depositar(saldo = saldo, valor = valor, extrato = extrato)
           
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError: 
                print("Valor inválido")
                continue
            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato, LIMITE_SAQUES = LIMITE_DIARIO, numero_saques = len(historico_saque))

            
            
        elif opcao == "e":
            
            exibe_extrato(saldo, extrato =extrato)

        elif opcao == "c":
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, usuarios)
            if conta:
                contas.append(conta)

        
        elif opcao == "u":
            criar_usuario(usuarios)
            
        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        else:
            print("Opção inválida")
            continue
    
if __name__ == "__main__":
    main()
