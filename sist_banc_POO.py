from datetime import date
from abc import ABC, abstractmethod, abstractproperty
import textwrap

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self):
        pass


class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao._valor,
                "data": date.today().strftime("%d/%m/%Y"),
            }
        )

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '001'
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    @property
    def saldo(self)-> float:
        return self._saldo
    def sacar(self, valor):
        if valor > self._saldo:
            print('saldo insuficiente')
            return False
        if valor >0:
            self._saldo -= valor
            print('saque realizado com sucesso\n')
            return True
        else:
            print('valor inválido\n')
            
        return False
    def depositar(self, valor):
        if valor >0:
            self._saldo += valor
            print('deposito realizado com sucesso\n')
        else:
            print('valor inválido\n')
            return False
            
        return True
        
    
    

    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def sacar(self,valor):
        
        numero_saques = len([transacao for transacao in self.historico.transacoes if
                             transacao['tipo'] == Saque.__name__])
        
        
        
        if valor> self._limite:
            print('Limite de saque excedido')
            return False
        elif numero_saques >= self._limite_saques:
            print('Limite de saques atingido')
            return False

        elif valor > 0:
            return super().sacar(valor)
        
        return False
    
    


    def __str__(self):
        return f""" Agência: {self._agencia}
                    \nC/C: {self.numero}
                    \nTitular: {self._cliente._nome}
                    """

    
class Pessoa_Fisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome:str, data_nascimento: date):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome   
        self._data_nascimento = data_nascimento
        
        
class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            conta._historico.adicionar_transacao(self)
        
        
        
class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.depositar(self._valor)
        if sucesso:
            conta._historico.adicionar_transacao(self)
    
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


def sacar(clientes):
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_usuario(cpf, clientes)
    if not cliente:
        print("Usuario nao encontrado")
        return
    valor = float(input("Informe o valor do saque: "))
    
    transacao = Saque(valor)
    conta = recuperar_conta(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)
    

    
def depositar(clientes):
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = filtrar_usuario(cpf, clientes)
    if not cliente:
        print("Usuario nao encontrado")
        return
    valor = float(input("Informe o valor do deposito: "))
    
    transacao = Deposito(valor)
    conta = recuperar_conta(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)
    
def recuperar_conta(cliente):
    if not cliente.contas:
        print("Cliente nao possui contas")
        return
    return cliente.contas[0]

def exibe_extrato(clientes):
    cpf = input('Informe o CPF do titular da conta:')
    cliente = filtrar_usuario(cpf, clientes)
    if not cliente:
        print('Usuario nao encontrado')
        return
    conta = recuperar_conta(cliente)
    if not conta:
        return
    print('EXTRATO:\n')
    transacoes = conta._historico.transacoes
    extrato = ''    
    if not transacoes:
        print('Nao foram realizadas movimentacoes')
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R${transacao['valor']:.2f}\n"
    print(extrato)
    print(f'Saldo: R${conta._saldo:.2f}')



    

def criar_clientes(usuaios):
    """sem usuarios repetido"""
    
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuaios)
    
    if usuario:
        print(f'Usuario {usuario["nome"]} já cadastrado')
        return
    nome = input('Informe o nome completo:')
    data_nascimento = input('Informe a data de nascimento:')
    endereco = input('Informe o endereço no formato: logadouro, numero, bairro, cidade/sigla estado:')
    
    
    cliente = Pessoa_Fisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco, cpf=cpf)
    usuaios.append(cliente)   
    print('Usuario criado com sucesso')
    
    
    
    
def filtrar_usuario(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(num_conta, clientes, contas):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, clientes)
    if not usuario:
        print("Usuario nao encontrado")
    conta = ContaCorrente.nova_conta(cliente = usuario, numero = num_conta)
    contas.append(conta)
    usuario.contas.append(conta)    
    print('conta criada com sucesso')
    
def listar_contas(contas):
   for conta in contas:
       print("=" * 100)
       print(textwrap.dedent(str(conta)))






def main():
    
    clientes = []
    contas = []
    
    while True:
        opcao = menu()

        
        if opcao == "d":
            depositar(clientes)
      
        elif opcao == "s":
            
            sacar(clientes)
            
            
        elif opcao == "e":
            
            exibe_extrato(clientes)

        elif opcao == "c":
            numero_conta = len(contas)+1
            
            criar_conta(numero_conta, clientes, contas)

        
        elif opcao == "u":
            criar_clientes(clientes)
            
        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        else:
            print("Opção inválida")
            continue
    
if __name__ == "__main__":
    main()
