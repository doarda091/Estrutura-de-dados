class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = 5
altura = 3
retangulo = Retangulo(base, altura)
area = retangulo.calcular_area()
print(f"A área do retângulo com base {base} e altura {altura} é {area}")
