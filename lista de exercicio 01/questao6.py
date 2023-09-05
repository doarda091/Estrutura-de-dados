#Calcule a fatorial de um número
def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

#Função principal
def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        resultado = calcular_fatorial(numero)

        if isinstance(resultado, int):
            print(f"O fatorial de {numero} é {resultado}.")
        else:
            print(resultado)
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro positivo.")

if __name__ == "__main__":
    main()
