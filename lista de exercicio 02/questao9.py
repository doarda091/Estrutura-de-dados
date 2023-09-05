class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

triangulo1 = Triangulo(3, 4, 5)
triangulo2 = Triangulo(7, 8, 9)

perimetro_tri1 = triangulo1.calcular_perimetro()
perimetro_tri2 = triangulo2.calcular_perimetro()

print(f"Triângulo 1: Lados = {triangulo1.lado1}, {triangulo1.lado2}, {triangulo1.lado3}")
print(f"Perímetro do Triângulo 1: {perimetro_tri1}")

print(f"Triângulo 2: Lados = {triangulo2.lado1}, {triangulo2.lado2}, {triangulo2.lado3}")
print(f"Perímetro do Triângulo 2: {perimetro_tri2}")
