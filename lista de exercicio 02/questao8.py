class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0.0
        else:
            soma = sum(self.notas)
            media = soma / len(self.notas)
            return media

notas_aluno1 = [8.5, 9.0, 7.5, 8.0]
notas_aluno2 = [9.5, 9.5, 9.0, 9.5]

aluno1 = Aluno("Maria", notas_aluno1)
aluno2 = Aluno("João", notas_aluno2)

media_aluno1 = aluno1.calcular_media()
media_aluno2 = aluno2.calcular_media()

print(f"Aluno: {aluno1.nome}, Média das Notas: {media_aluno1:.2f}")
print(f"Aluno: {aluno2.nome}, Média das Notas: {media_aluno2:.2f}")
