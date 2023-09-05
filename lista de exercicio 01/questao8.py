#Verifique se o número é primo
def eh_primo(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Encontrou um divisor, portanto não é primo

    return True  # Se não encontrou divisores, é primo

#Função principal
def main():
    try:
        numero = int(input("Digite um número inteiro positivo para verificar se é primo: "))

        if numero <= 0:
            print("Por favor, insira um número inteiro positivo maior que 1.")
        else:
            if eh_primo(numero):
                print(numero, "é um número primo.")
            else:
                print(numero, "não é um número primo.")

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro positivo.")

if __name__ == "__main__":
    main()
