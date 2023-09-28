import queue
import threading
import time

fila_de_atendimento = queue.Queue()

def adicionar_cliente(cliente):
    fila_de_atendimento.put(cliente)
    print(f"Cliente {cliente} entrou na fila de atendimento.")

def atender_clientes():
    while True:
        if not fila_de_atendimento.empty():
            cliente = fila_de_atendimento.get()
            print(f"Funcionário está atendendo o cliente {cliente}.")
            time.sleep(2)
            print(f"Cliente {cliente} foi atendido.")
        else:
            print("Não há clientes na fila de atendimento. Funcionário está ocioso.")
            time.sleep(1)

for i in range(1, 6):
    adicionar_cliente(i)
    time.sleep(1)

funcionario = threading.Thread(target=atender_clientes)

funcionario.start()

funcionario.join()

print("Atendimento encerrado. Todos os clientes foram atendidos.")
