def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("O número deve ser positivo.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro positivo.")
