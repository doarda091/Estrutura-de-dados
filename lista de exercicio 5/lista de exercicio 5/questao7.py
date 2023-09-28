class CalculadoraRPN:
    def __init__(self):
        self.pilha = []

    def avaliar_rpn(self, expressao):
        tokens = expressao.split()
        operadores = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operadores:
                self.pilha.append(float(token))
            else:
                if len(self.pilha) < 2:
                    return "Expressão inválida"
                b = self.pilha.pop()
                a = self.pilha.pop()
                resultado = self.calcular(a, b, token)
                self.pilha.append(resultado)

        if len(self.pilha) == 1:
            return self.pilha[0]
        else:
            return "Expressão inválida"

    def calcular(self, a, b, operador):
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            if b != 0:
                return a / b
            else:
                return "Divisão por zero"

calculadora = CalculadoraRPN()

expressao1 = "3 4 + 2 *"
resultado1 = calculadora.avaliar_rpn(expressao1)
print("Resultado da expressão 1:", resultado1)

expressao2 = "5 2 4 * + 7 -"
resultado2 = calculadora.avaliar_rpn(expressao2)
print("Resultado da expressão 2:", resultado2)

expressao3 = "2 0 /"
resultado3 = calculadora.avaliar_rpn(expressao3)
print("Resultado da expressão 3:", resultado3)
