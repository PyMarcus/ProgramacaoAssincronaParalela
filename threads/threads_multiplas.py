# threads multiplas são várias linhas de execução para executar partes do programa
import threading
import time


def main():
    # passa-se uma listas de threads para ser iniciada
    ths = [threading.Thread(target=conte, args=('Reais', 10)), # A ordem e o tempo não são decididos por mim, mas pelo algoritmo de escalonamento do SO
           threading.Thread(target=conte, args=('Dólares', 8)),
           threading.Thread(target=conte, args=('Euros', 20)),
           threading.Thread(target=conte, args=('centavos', 1)),
           threading.Thread(target=conte, args=('moedas de ouro', 5))]  # cada thread será executada ao mesmo tempo, usando os cores do processador.O funcionamento é semelhante ao de thread simples
    print("Começou")
    [thss.start() for thss in ths]
    print("rodando em segundo plano")
    [thss.join() for thss in ths]
    assert len(ths) == 5  # se falso, gera um erro
    print("acabou")
    "ok"


def conte(argumento1, argumento2):
    for n in range(2, argumento2 + 1):
        print(f"{argumento1} {n}")
        time.sleep(1)


if __name__ == '__main__':
    main()
