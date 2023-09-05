class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            aumento = (percentual_aumento / 100) * self.salario
            self.salario += aumento
            print(f"O salário de {self.nome} foi aumentado em {percentual_aumento}%")
            print(f"Novo salário de {self.nome}: R${self.salario:.2f}")
        else:
            print("O percentual de aumento deve ser maior que zero.")

funcionario1 = Funcionario("Maria", 5000, "Analista")
funcionario2 = Funcionario("João", 6000, "Gerente")

funcionario1.aumentar_salario(10)  # Aumento de 10%
funcionario2.aumentar_salario(5)   # Aumento de 5%
