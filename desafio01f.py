import datetime
import os

class ContaBancaria:
    LIMITE_SAQUES_DIARIOS = 3
    LIMITE_VALOR_SAQUE = 500.00

    def __init__(self):
        self.saldo = 0.0
        self.movimentacoes = []  # lista de tuplas: (data, tipo, valor)
        self.saques_hoje = 0
        self.data_ultimo_saque = None

    def depositar(self, valor: float):
        if valor <= 0:
            print("❌ Valor de depósito inválido. Informe um valor positivo.")
            return
        self.saldo += valor
        self.movimentacoes.append((datetime.datetime.now(), 'Depósito', valor))
        print(f"✅ Depósito realizado: R$ {valor:.2f}")

    def sacar(self, valor: float):
        hoje = datetime.date.today()

        if self.data_ultimo_saque != hoje:
            self.saques_hoje = 0
            self.data_ultimo_saque = hoje

        if valor <= 0:
            print("❌ Valor de saque inválido. Informe um valor positivo.")
            return
        if valor > self.LIMITE_VALOR_SAQUE:
            print(f"❌ Saque não permitido: valor máximo por saque é R$ {self.LIMITE_VALOR_SAQUE:.2f}.")
            return
        if self.saques_hoje >= self.LIMITE_SAQUES_DIARIOS:
            print("❌ Limite diário de saques atingido.")
            return
        if valor > self.saldo:
            print("❌ Saldo insuficiente para saque.")
            return

        self.saldo -= valor
        self.saques_hoje += 1
        self.movimentacoes.append((datetime.datetime.now(), 'Saque', -valor))
        print(f"✅ Saque realizado: R$ {valor:.2f}")

    def extrato(self):
        print("\n======= EXTRATO =======")
        if not self.movimentacoes:
            print("Não foram realizadas movimentações.")
        else:
            for data, tipo, valor in self.movimentacoes:
                print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {tipo}: R$ {abs(valor):.2f}")
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("========================\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    conta = ContaBancaria()

    while True:
        print("=== BANCO PYTHON ===")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        limpar_tela()

        if opcao == '1':
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("❌ Entrada inválida. Use apenas números.")
        elif opcao == '2':
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print("❌ Entrada inválida. Use apenas números.")
        elif opcao == '3':
            conta.extrato()
        elif opcao == '0':
            print("Obrigado por usar o Banco Python!")
            break
        else:
            print("❌ Opção inválida.")

        input("\nPressione Enter para continuar...")
        limpar_tela()

if __name__ == "__main__":
    menu()
