def ordenar_por_selecao(vetor):
    n = len(vetor)

    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j

        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

vetor = [64, 25, 12, 22, 11]
print("Vetor original:", vetor)

ordenar_por_selecao(vetor)

print("Vetor ordenado:", vetor)
