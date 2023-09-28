class FilaDePedidos:
    def __init__(self):
        self.fila = []

    def adicionar_pedido(self, pedido):
        """
        Adiciona um pedido à fila.
        """
        self.fila.append(pedido)
        print(f"Pedido {pedido} adicionado à fila.")

    def processar_pedido(self):
        """
        Processa o pedido mais antigo na fila e o remove da fila.
        """
        if self.fila:
            pedido_processado = self.fila.pop(0)
            print(f"Pedido {pedido_processado} processado com sucesso.")
        else:
            print("A fila de pedidos está vazia.")

    def mostrar_fila(self):
        """
        Mostra os pedidos na fila.
        """
        if self.fila:
            print("Fila de Pedidos:")
            for pedido in self.fila:
                print(pedido)
        else:
            print("A fila de pedidos está vazia.")

fila_pedidos = FilaDePedidos()
fila_pedidos.adicionar_pedido("Pedido 1")
fila_pedidos.adicionar_pedido("Pedido 2")
fila_pedidos.mostrar_fila()
fila_pedidos.processar_pedido()
fila_pedidos.mostrar_fila()
fila_pedidos.processar_pedido()
fila_pedidos.mostrar_fila()
