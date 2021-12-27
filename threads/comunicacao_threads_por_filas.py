# threads comunicam via queues (filas = entrada e saida no inicio, armazenamento ao final)

# exemplo, dado uma thread para cada funcao, mas os dados usados simultaneamente:
import time
from threading import Thread
from queue import Queue  # fila
from colorama import Fore


def gera_dados(queue):
    for i in range(1, 11):
        print(Fore.GREEN + f"Dados {i} gerados", flush=True)
        time.sleep(2)
        queue.put(i)


def consumidor_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()  # devolve o valor e remove da fila
        print(Fore.RED + f"Dado {valor * 2} processado", flush=True)
        time.sleep(1)
        queue.task_done() # ao remover um dado, vai concluíndo a tarefa


if __name__ == '__main__':
    print("sistema iniciado", flush=True)
    queue = Queue()
    th1 = Thread(target=gera_dados, args=(queue,))
    th2 = Thread(target=consumidor_dados, args=(queue,))
    th1.start()
    th1.join() # gera os dados 1, alimentando as threads
    th2.start()
    th2.join()
