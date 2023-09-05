import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        if self.raio < 0:
            return "O raio não pode ser negativo."
        else:
            area = math.pi * self.raio**2
            return area

if __name__ == "__main__":
    raio_circulo = float(input("Digite o raio do círculo: "))
    circulo = Circulo(raio_circulo)
    
    area_circulo = circulo.calcular_area()
    
    if isinstance(area_circulo, str):
        print(area_circulo)
    else:
        print(f"A área do círculo com raio {raio_circulo} é {area_circulo:.2f}.")
