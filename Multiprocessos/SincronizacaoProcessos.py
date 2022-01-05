"""
Forma de executar processos concorrentes sem afetar o código de forma crítica
ou seja, nao acessa valores e os altera interferindo no processo como um todo
"""
import multiprocessing
import ctypes


def depositar(saldo):
    for _ in range(10_000):
        saldo.value += 1


def sacar(saldo):
    for _ in range(10_000):
        saldo.value -= saldo.value


def realizar_transacoes(saldo):
    p1 = multiprocessing.Process(target=depositar, args=(saldo,))
    p2 = multiprocessing.Process(target=sacar, args=(saldo,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # com value, ocorre race conditions, que é quando uma thread interfere na outra


if __name__ == '__main__':
    saldo = multiprocessing.Value("i", 100)
    print(f"Saldo inicial: {saldo.value}")
    for _ in range(10):
        realizar_transacoes(saldo)
    print(
        f"Saldo final: {saldo.value}")  # retorna 0, pois, pegou acrescentou 10000, mas retirou em seguida, alterando a variavel
