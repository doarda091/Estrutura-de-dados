def calcular_mediana(vetor):
    n = len(vetor)
    
    if n % 2 == 0:
        indice_meio1 = n // 2 - 1
        indice_meio2 = n // 2
        mediana = (vetor[indice_meio1] + vetor[indice_meio2]) / 2
    else:
        indice_meio = n // 2
        mediana = vetor[indice_meio]
    
    return mediana

vetor = [64, 25, 12, 22, 11, 25, 11, 64]

mediana = calcular_mediana(vetor)

print("Vetor:", vetor)
print("Mediana:", mediana)
