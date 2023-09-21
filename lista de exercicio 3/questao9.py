def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = int(input("Digite o número da operação desejada: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == 1:
    resultado = adicao(num1, num2)
    operacao = "adição"
elif escolha == 2:
    resultado = subtracao(num1, num2)
    operacao = "subtração"
elif escolha == 3:
    resultado = multiplicacao(num1, num2)
    operacao = "multiplicação"
elif escolha == 4:
    resultado = divisao(num1, num2)
    operacao = "divisão"
else:
    print("Opção inválida. Por favor, escolha um número de 1 a 4 para a operação.")
    resultado = None

if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")
