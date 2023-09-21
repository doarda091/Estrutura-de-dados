def segundo_menor(vetor):
    if len(vetor) < 2:
        return None

    vetor_sem_duplicatas = list(set(vetor))

    if len(vetor_sem_duplicatas) < 2:
        return None
    vetor_ordenado = sorted(vetor_sem_duplicatas)

    return vetor_ordenado[1]
vetor = [64, 25, 12, 22, 11, 25, 11, 64]

segundo_menor_numero = segundo_menor(vetor)

if segundo_menor_numero is not None:
    print("Vetor:", vetor)
    print("Segundo menor número:", segundo_menor_numero)
else:
    print("Não foi possível encontrar o segundo menor número no vetor.")
