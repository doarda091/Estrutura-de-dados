import queue
import threading
import time

fila_de_tarefas = queue.Queue()

def adicionar_tarefa(tarefa):
    fila_de_tarefas.put(tarefa)
    print(f"Tarefa adicionada à lista de tarefas pendentes: {tarefa}")

def concluir_tarefas():
    while True:
        if not fila_de_tarefas.empty():
            tarefa = fila_de_tarefas.get()
            print(f"Concluindo a tarefa: {tarefa}")
            time.sleep(2)
            print(f"Tarefa concluída: {tarefa}")
        else:
            print("Não há tarefas pendentes para concluir.")
            time.sleep(1)

for i in range(1, 6):
    adicionar_tarefa(f"Tarefa {i}")
    time.sleep(1)

executor = threading.Thread(target=concluir_tarefas)

executor.start()

executor.join()

print("Todas as tarefas pendentes foram concluídas.")
