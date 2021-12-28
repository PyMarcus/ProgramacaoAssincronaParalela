# melhor método, pois é mais seguro
import multiprocessing


# a comunicação entre processos pode ser feita utilizando filas,queues, e pipes
def ping(queue) -> None:
    """Faz o envio da informação em um lado do pipe"""
    print(multiprocessing.current_process().name)
    queue.put("Marcus")


def pong(queue) -> None:
    """Recebe o envio da informação em outro lado do pipe"""
    msg = queue.get()
    print(multiprocessing.current_process().name)
    print(f"{msg} Vinícius")


def main():
    queue = multiprocessing.Queue()
    processo1 = multiprocessing.Process(target=ping, args=(queue,))
    processo2 = multiprocessing.Process(target=pong, args=(queue,))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()


if __name__ == '__main__':
    main()
