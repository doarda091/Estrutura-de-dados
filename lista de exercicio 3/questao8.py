print("Escolha o tipo de conversão:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

escolha = int(input("Digite o número da opção desejada: "))

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius são {fahrenheit} graus Fahrenheit.")
    
elif escolha == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")
    
else:
    print("Opção inválida. Por favor, escolha 1 ou 2 para a conversão.")
