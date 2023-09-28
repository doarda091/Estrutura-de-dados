class NavegadorWeb:
    def __init__(self):
        self.paginas_visitadas = []
        self.indice_atual = -1

    def abrir_pagina(self, url):
        """
        Abre uma nova página e adiciona ao histórico.
        """
        if self.indice_atual < len(self.paginas_visitadas) - 1:
            self.paginas_visitadas = self.paginas_visitadas[:self.indice_atual + 1]

        self.paginas_visitadas.append(url)
        self.indice_atual += 1

    def voltar(self):
        """
        Navega para a página anterior no histórico.
        """
        if self.indice_atual > 0:
            self.indice_atual -= 1
            return self.paginas_visitadas[self.indice_atual]
        else:
            return "Não é possível voltar mais."

    def avancar(self):
        """
        Navega para a próxima página no histórico.
        """
        if self.indice_atual < len(self.paginas_visitadas) - 1:
            self.indice_atual += 1
            return self.paginas_visitadas[self.indice_atual]
        else:
            return "Não é possível avançar mais."

    def mostrar_pagina_atual(self):
        """
        Exibe a página atual.
        """
        if self.indice_atual >= 0:
            return self.paginas_visitadas[self.indice_atual]
        else:
            return "Nenhuma página aberta."

navegador = NavegadorWeb()
navegador.abrir_pagina("https://www.exemplo.com")
navegador.abrir_pagina("https://www.openai.com")
navegador.abrir_pagina("https://www.python.org")

print("Página atual:", navegador.mostrar_pagina_atual())

print("Voltar:", navegador.voltar())
print("Voltar:", navegador.voltar())

print("Avançar:", navegador.avancar())

navegador.abrir_pagina("https://www.github.com")
print("Página atual:", navegador.mostrar_pagina_atual())
