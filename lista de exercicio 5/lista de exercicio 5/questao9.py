class ExpressaoMatematica:
    def __init__(self, expressao):
        self.expressao = expressao

    def encontrar_operadores(self):
        operadores = set("+-*/^()")
        pilha = []

        for char in self.expressao:
            if char in operadores:
                pilha.append(char)

        operadores_encontrados = list(set(pilha))
        operadores_encontrados.sort()

        return operadores_encontrados

expressao = "(2+3)*(8-9)/(7^3)"
analise = ExpressaoMatematica(expressao)
operadores = analise.encontrar_operadores()

print("Operadores matemáticos na expressão:")
print(operadores)
