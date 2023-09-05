class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.nome} diz: 'Olá, como você está?'")

pessoa1 = Pessoa("Maria", 30)
pessoa2 = Pessoa("João", 25)

pessoa1.falar()
pessoa2.falar()
