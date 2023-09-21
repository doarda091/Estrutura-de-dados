def terceiro_maior(vetor):
    if len(vetor) < 3:
        return None
    vetor_sem_duplicatas = list(set(vetor))

    if len(vetor_sem_duplicatas) < 3:
        return None

    vetor_sem_duplicatas.sort(reverse=True)

    return vetor_sem_duplicatas[2]

vetor = [64, 25, 12, 22, 11, 25, 11, 64]

terceiro_maior_numero = terceiro_maior(vetor)

if terceiro_maior_numero is not None:
    print("Vetor:", vetor)
    print("Terceiro maior número:", terceiro_maior_numero)
else:
    print("Não foi possível encontrar o terceiro maior número no vetor.")
