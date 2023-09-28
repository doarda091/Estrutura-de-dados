import queue
import threading
import time

fila_de_pedidos = queue.Queue()

def fazer_pedido(cliente, item):
    pedido = (cliente, item)
    fila_de_pedidos.put(pedido)
    print(f"Cliente {cliente} fez um pedido: {item}")

def processar_pedidos():
    while True:
        if not fila_de_pedidos.empty():
            cliente, item = fila_de_pedidos.get()
            print(f"Preparando pedido de {cliente}: {item}")
            time.sleep(2)
            print(f"Pedido de {cliente}: {item} pronto para servir.")
        else:
            print("Não há pedidos a serem processados no momento.")
            time.sleep(1)

for i in range(1, 6):
    fazer_pedido(f"Cliente {i}", f"Prato {i}")
    time.sleep(1)

cozinheiro = threading.Thread(target=processar_pedidos)

cozinheiro.start()

cozinheiro.join()

print("Todos os pedidos foram processados e estão prontos para servir.")
