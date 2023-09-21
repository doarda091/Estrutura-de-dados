def remover_duplicatas(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    return vetor_sem_duplicatas

vetor = [64, 25, 12, 22, 11, 25, 11, 64]

vetor_sem_duplicatas = remover_duplicatas(vetor)

print("Vetor original:", vetor)
print("Vetor sem duplicatas:", vetor_sem_duplicatas)
