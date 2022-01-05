import multiprocessing
import ctypes

# agora, fazendo eles compartilharem memória, por isso, usa C


def funcao1(valor, estado):
    if estado.value:  # .value acessa o valor com ctypes
        valor.value += 10
        estado.value = False
    else:
        valor.value += 20
        estado.value = True
    print(f"Resultado {valor.value}")


def funcao2(valor, estado):
    if estado.value:
        valor.value += 30
        estado.value = False
    else:
        valor.value += 40
        estado.value = True
    print(f"Resultado {valor.value}")


def main():
    x = multiprocessing.Value('i', 5)
    y = multiprocessing.Value(ctypes.c_bool, True)
    p1 = multiprocessing.Process(target=funcao1, args=(x, y))  # mesmo usando as mesmas variáveis, a passagem de parâmetros se da por cópias
    p2 = multiprocessing.Process(target=funcao2, args=(x, y))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
