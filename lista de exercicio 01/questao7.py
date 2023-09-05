#Gere a sequência de Fibonacci até um determinado valor
def fibonacci_ate_n(n):
    fibonacci = [0, 1]  # Inicializando com os dois primeiros números da sequência

    while fibonacci[-1] + fibonacci[-2] <= n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)

    return fibonacci

#Função principal
def main():
    try:
        limite = int(input("Digite um valor limite para a sequência de Fibonacci: "))

        if limite < 0:
            print("Por favor, insira um valor não negativo.")
        else:
            sequencia_fibonacci = fibonacci_ate_n(limite)

            if sequencia_fibonacci:
                print("Sequência de Fibonacci até", limite, ":")
                for numero in sequencia_fibonacci:
                    print(numero, end=" ")
                print()
            else:
                print("Não há números na sequência de Fibonacci até", limite)

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro não negativo.")

if __name__ == "__main__":
    main()
