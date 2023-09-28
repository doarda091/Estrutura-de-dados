class EditorDeTexto:
    def __init__(self):
        self.texto = ""
        self.historico_undo = []
        self.historico_redo = []
    def inserir_texto(self, texto_inserido):
        self.texto += texto_inserido
        self.historico_undo.append(("inserir", texto_inserido))
        self.historico_redo = []

    def apagar_texto(self, num_caracteres):
        if num_caracteres > len(self.texto):
            num_caracteres = len(self.texto)
        texto_apagado = self.texto[-num_caracteres:]
        self.texto = self.texto[:-num_caracteres]
        self.historico_undo.append(("apagar", texto_apagado))
        self.historico_redo = []

    def desfazer(self):
        if self.historico_undo:
            comando, texto = self.historico_undo.pop()
            if comando == "inserir":
                self.texto = self.texto[:-len(texto)]
            elif comando == "apagar":
                self.texto += texto
            self.historico_redo.append((comando, texto))

    def refazer(self):
        if self.historico_redo:
            comando, texto = self.historico_redo.pop()
            if comando == "inserir":
                self.texto += texto
            elif comando == "apagar":
                self.texto = self.texto[:-len(texto)]
            self.historico_undo.append((comando, texto))

    def mostrar_texto(self):
        return self.texto

editor = EditorDeTexto()
editor.inserir_texto("Olá, mundo! ")
editor.inserir_texto("Isso é uma implementação simples de um editor de texto em Python.")
print("Texto atual:")
print(editor.mostrar_texto())

editor.apagar_texto(15)
print("Texto após apagar:")
print(editor.mostrar_texto())

editor.desfazer()
print("Texto após desfazer:")
print(editor.mostrar_texto())

editor.refazer()
print("Texto após refazer:")
print(editor.mostrar_texto())
