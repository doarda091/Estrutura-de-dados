def ordenar_vetor(vetor, ordem_crescente=True):
    """
    Ordena um vetor de inteiros em ordem crescente ou decrescente, dependendo do parâmetro 'ordem_crescente'.
    
    Args:
    vetor (list): O vetor de inteiros a ser ordenado.
    ordem_crescente (bool): Se True, a ordenação será em ordem crescente. Se False, em ordem decrescente.
    
    Returns:
    list: O vetor ordenado.
    """
    n = len(vetor)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ordem_crescente:
                if vetor[j] > vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
            else:
                if vetor[j] < vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    
    return vetor

vetor_crescente = [64, 25, 12, 22, 11]
print("Vetor original (crescente):", vetor_crescente)
vetor_crescente_ordenado = ordenar_vetor(vetor_crescente)
print("Vetor ordenado (crescente):", vetor_crescente_ordenado)

vetor_decrescente = [64, 25, 12, 22, 11]
print("Vetor original (decrescente):", vetor_decrescente)
vetor_decrescente_ordenado = ordenar_vetor(vetor_decrescente, ordem_crescente=False)
print("Vetor ordenado (decrescente):", vetor_decrescente_ordenado)
