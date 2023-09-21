numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    soma = 0

    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10

    print(f"A soma dos dígitos é: {soma}")
