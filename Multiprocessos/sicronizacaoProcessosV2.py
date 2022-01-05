"""
Forma de executar processos concorrentes sem afetar o código de forma crítica
ou seja, nao acessa valores e os altera interferindo no processo como um todo
"""
import multiprocessing
import ctypes


def depositar(saldo, lock):
    for _ in range(10_000):
        with lock: # lock impede de ocorrer race conditions, e a thread terminar o processo
            saldo.value = saldo.value + 1


def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1


def realizar_transacoes(saldo, lock):
    p1 = multiprocessing.Process(target=depositar, args=(saldo, lock))
    p2 = multiprocessing.Process(target=sacar, args=(saldo, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # com value, ocorre race conditions, que é quando uma thread interfere na outra


if __name__ == '__main__':
    saldo = multiprocessing.Value("i", 100)
    lock = multiprocessing.RLock()
    print(f"Saldo inicial: {saldo.value}")
    for _ in range(10):
        realizar_transacoes(saldo, lock)
    print(
        f"Saldo final: {saldo.value}")  # retorna 0, pois, pegou acrescentou 10000, mas retirou em seguida, alterando a variavel
