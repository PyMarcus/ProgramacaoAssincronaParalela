import multiprocessing


# a comunicação entre processos pode ser feita utilizando filas,queues, e pipes
def ping(conexao) -> None:
    """Faz o envio da informação em um lado do pipe"""
    print(multiprocessing.current_process().name)
    conexao.send("Marcus")


def pong(conexao) -> None:
    """Recebe o envio da informação em outro lado do pipe"""
    msg = conexao.recv()
    print(multiprocessing.current_process().name)
    print(f"{msg} Vinícius")


def main():
    conexao1, conexao2 = multiprocessing.Pipe(True) # true tanto pode enviar quanto receber, falso restringe
    processo1 = multiprocessing.Process(target=ping, args=(conexao1,))
    processo2 = multiprocessing.Process(target=pong, args=(conexao2, ))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

if __name__ == '__main__':
    main()