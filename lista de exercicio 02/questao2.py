class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

if __name__ == "__main__":
    titulo_livro = input("Digite o título do livro: ")
    autor_livro = input("Digite o nome do autor do livro: ")
    
    livro = Livro(titulo_livro, autor_livro)
    
    informacoes_livro = livro.detalhes()
    print("Detalhes do livro:")
    print(informacoes_livro)
