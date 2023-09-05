class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")

conta = ContaBancaria("João")
print(f"Conta de {conta.titular} - Saldo inicial: R${conta.saldo}")

conta.depositar(1000)
conta.sacar(500)
conta.sacar(800)
