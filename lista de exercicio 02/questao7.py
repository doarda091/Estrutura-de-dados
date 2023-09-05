class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

carro1 = Carro("Toyota", "Corolla", 2022)
carro2 = Carro("Ford", "Mustang", 2023)

detalhes_carro1 = carro1.detalhes()
detalhes_carro2 = carro2.detalhes()

print(detalhes_carro1)
print(detalhes_carro2)
