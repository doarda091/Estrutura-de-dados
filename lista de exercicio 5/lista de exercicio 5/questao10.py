class VerificadorPalindromo:
    def __init__(self):
        self.pilha = []

    def verificar_palindromo(self, texto):
        texto = texto.replace(" ", "").lower()

        for char in texto:
            self.pilha.append(char)

        pilha_invertida = list(reversed(self.pilha))

        if self.pilha == pilha_invertida:
            return True
        else:
            return False

verificador = VerificadorPalindromo()

palavra = "radar"
resultado = verificador.verificar_palindromo(palavra)
if resultado:
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")

frase = "A man, a plan, a canal, Panama"
resultado = verificador.verificar_palindromo(frase)
if resultado:
    print(f"'{frase}' é um palíndromo.")
else:
    print(f"'{frase}' não é um palíndromo.")
