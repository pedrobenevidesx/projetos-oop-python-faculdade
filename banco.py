import csv
import os

# Arquivos
CADASTRO_FILE = "cadastro.csv"
DADOS_FILE = "dados.csv"

# ---------------- Funções ----------------

# Carregar clientes
def carregar_clientes():
    clientes = {}
    if os.path.exists(CADASTRO_FILE):
        arquivo = open(CADASTRO_FILE, "r", encoding="utf-8")
        leitor = csv.reader(arquivo, delimiter=';')
        next(leitor)  # pula o cabeçalho
        for linha in leitor:
            nome = linha[0].strip().lower()       # pega o nome
            saldo = float(linha[4])              # pega o saldo_inicial
            clientes[nome] = saldo
        arquivo.close()
    return clientes

# Salvar clientes
def salvar_clientes(clientes):
    arquivo = open(CADASTRO_FILE, "w", newline='', encoding="utf-8")
    escritor = csv.writer(arquivo, delimiter=';')
    escritor.writerow(["nome","banco","agencia","conta","saldo_inicial"])
    for nome, saldo in clientes.items():
        escritor.writerow([nome.title(),"","","", saldo])  # deixa os outros campos vazios
    arquivo.close()

# Registrar operação
def registrar_operacao(tipo, origem, destino, valor):
    arquivo = open(DADOS_FILE, "a", newline='', encoding="utf-8")
    escritor = csv.writer(arquivo, delimiter=';')
    if os.stat(DADOS_FILE).st_size == 0:
        escritor.writerow(["tipo","origem","destino","valor"])
    escritor.writerow([tipo, origem.title(), destino.title(), valor])
    arquivo.close()

# Saque
def sacar(clientes, nome, valor):
    chave = nome.strip().lower()
    if chave not in clientes:
        print("Cliente não encontrado!")
        return
    if clientes[chave] < valor:
        print("Saldo insuficiente!")
        return
    clientes[chave] -= valor
    registrar_operacao("saque", chave, "-", valor)
    print(f"Saque realizado! Saldo atual: R${clientes[chave]:.2f}")

# Depósito
def depositar(clientes, nome, valor):
    chave = nome.strip().lower()
    if chave not in clientes:
        print("Cliente não encontrado!")
        return
    clientes[chave] += valor
    registrar_operacao("deposito", "-", chave, valor)
    print(f"Depósito realizado! Saldo atual: R${clientes[chave]:.2f}")

# Transferência
def transferir(clientes, origem, destino, valor):
    c_origem = origem.strip().lower()
    c_destino = destino.strip().lower()
    if c_origem not in clientes or c_destino not in clientes:
        print("Cliente(s) não encontrado(s)!")
        return
    if clientes[c_origem] < valor:
        print("Saldo insuficiente!")
        return
    clientes[c_origem] -= valor
    clientes[c_destino] += valor
    registrar_operacao("transferencia", c_origem, c_destino, valor)
    print("Transferência realizada!")

# Histórico
def exibir_historico():
    if not os.path.exists(DADOS_FILE):
        print("Nenhuma operação registrada!")
        return
    arquivo = open(DADOS_FILE, "r", encoding="utf-8")
    leitor = csv.reader(arquivo, delimiter=';')
    for linha in leitor:
        print(linha)
    arquivo.close()

# ---------------- Programa principal ----------------

def main():
    clientes = carregar_clientes()

    while True:
        print("\n--- Banco Simples ---")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Transferência")
        print("4 - Histórico")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            valor = float(input("Valor: "))
            sacar(clientes, nome, valor)
        elif opcao == "2":
            nome = input("Nome: ")
            valor = float(input("Valor: "))
            depositar(clientes, nome, valor)
        elif opcao == "3":
            origem = input("Origem: ")
            destino = input("Destino: ")
            valor = float(input("Valor: "))
            transferir(clientes, origem, destino, valor)
        elif opcao == "4":
            exibir_historico()
        elif opcao == "5":
            salvar_clientes(clientes)
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
