def ordenar_em_ordem_decrescente(vetor):
    vetor.sort(reverse=True)

def contar_pares_e_impares(vetor):
    numeros_pares = 0
    numeros_impares = 0

    for numero in vetor:
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

    return numeros_pares, numeros_impares

vetor = [64, 25, 12, 22, 11, 25, 11, 64]

ordenar_em_ordem_decrescente(vetor)
pares, impares = contar_pares_e_impares(vetor)

print("Vetor ordenado em ordem decrescente:", vetor)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
