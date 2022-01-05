# programa que visa abstrair os métodos de concorrencia
import threading
import time
import multiprocessing
from concurrent.futures.thread import ThreadPoolExecutor as Ex
from concurrent.futures.process import ProcessPoolExecutor as Ex1


def processa():
    lista = ["F", "O", "D", "A", "-", "S", "E"]
    print('[ ', end='', flush=True)
    t1 = time.perf_counter()
    for letras in lista:
        print(letras, end=' ', flush=True)
    print(']', end='', flush=True)
    t2 = time.perf_counter()
    print(t2 - t1)
    return 0


if __name__ == '__main__':
    th = threading.Thread(target=processa)
    th.start()
    th.join()

    mp = multiprocessing.Process(target=processa)
    mp.start()
    mp.join()  # mais rapido

    with Ex() as e:
        future = e.submit(processa)  # mais lento com time(),mas o mais rápido sem

    with Ex1() as e1:
        f = e1.submit(processa)
    print(f"RETORNO {f.result()}")