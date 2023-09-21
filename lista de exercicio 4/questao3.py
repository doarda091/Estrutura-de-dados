def encontrar_maximo(vetor):
    if len(vetor) == 0:
        return None
    
    maximo = vetor[0]
    
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    
    return maximo

def encontrar_minimo(vetor):
    if len(vetor) == 0:
        return None
    
    minimo = vetor[0]
    
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
    
    return minimo

vetor = [64, 25, 12, 22, 11]

elemento_maximo = encontrar_maximo(vetor)
elemento_minimo = encontrar_minimo(vetor)

print("Vetor:", vetor)
print("Elemento máximo:", elemento_maximo)
print("Elemento mínimo:", elemento_minimo)
