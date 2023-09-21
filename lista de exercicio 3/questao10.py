def sequencia_fibonacci(numero_termos):
    termo1 = 0
    termo2 = 1

    if numero_termos <= 0:
        print("Por favor, insira um número válido de termos.")
    elif numero_termos == 1:
        print("Sequência de Fibonacci:")
        print(termo1)
    else:
        print("Sequência de Fibonacci:")
        print(termo1, end=", ")
        print(termo2, end=", ")

        for _ in range(2, numero_termos):
            proximo_termo = termo1 + termo2
            print(proximo_termo, end=", ")

            termo1, termo2 = termo2, proximo_termo

numero_termos = int(input("Digite o número de termos da sequência de Fibonacci desejados: "))

sequencia_fibonacci(numero_termos)
