#Calcule a média dos números pares em uma lista
def media_numeros_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    if len(numeros_pares) == 0:
        return "Não há números pares na lista."
    else:
        soma = sum(numeros_pares)
        media = soma / len(numeros_pares)
        return media

#Função principal
def main():
    lista_numeros = []
    n = int(input("Quantos números você deseja adicionar à lista? "))

    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista_numeros.append(numero)

    resultado = media_numeros_pares(lista_numeros)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"A média dos números pares na lista é: {resultado:.2f}")

if __name__ == "__main__":
    main()
