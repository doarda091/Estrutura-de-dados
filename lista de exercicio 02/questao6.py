class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Camiseta", 20.0, 5)
produto2 = Produto("Calça", 50.0, 3)

total_produto1 = produto1.calcular_total()
total_produto2 = produto2.calcular_total()

print(f"Produto: {produto1.nome}, Preço: R${produto1.preco}, Quantidade: {produto1.quantidade}")
print(f"Total do Produto 1: R${total_produto1}")

print(f"Produto: {produto2.nome}, Preço: R${produto2.preco}, Quantidade: {produto2.quantidade}")
print(f"Total do Produto 2: R${total_produto2}")
