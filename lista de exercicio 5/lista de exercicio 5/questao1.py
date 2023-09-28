import queue

fila_de_impressao = queue.Queue()

def adicionar_documento(documento):
    fila_de_impressao.put(documento)
    print(f"Documento '{documento}' adicionado à fila de impressão.")

def imprimir_documentos():
    while not fila_de_impressao.empty():
        documento = fila_de_impressao.get()
        print(f"Imprimindo documento: {documento}")

adicionar_documento("Contrato 1")
adicionar_documento("Relatório Mensal")
adicionar_documento("Apresentação de slides")

print("Iniciando a impressão...")
imprimir_documentos()
