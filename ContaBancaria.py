class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo= saldo

    def __str__(self):
        return f"Titular: {self.titular} - Saldo: {self.saldo}"

    def depositar(self, valor): #nao passa saldo de novo, pois o saldo ja esta no objeto principal
        self.saldo += valor
        print(f"Deposito de {valor} reais realizado com sucesso")

    def sacar(self, valor): 
        self.saldo -= valor
        print(f"Saque de {valor} reais realizado com sucesso") 
        

banco = Banco("Any", 100)
print(banco)

banco.depositar(100)

print(banco)

banco.sacar(50)

print(banco)

        

        