"""
# o ideal é não compartilhar threads entre processos
# ctype tipos: c, u , i , I,f para char, string , inteiros e float
# nesse caso, compartilha-se valores(variaveis ou arrays), ou seja, memoria
--------------------------------------------------------------------------
Compartilhar valores únicos:
multiprocessing.Value
Compartilhar arrays(de mesmo tipo)
multiprocessing.Array
"""

# provando que os processos, por padrão ,não compartilham memória, mesmo usando o mesmo dado, isso , pois,
# o computador cria cópias das variáveis:
import multiprocessing
import time


def funcao1(valor, estado):
    if estado:
        valor += 10
        estado = False
    else:
        valor += 20
        estado = True
    print(f"Resultado {valor}")


def funcao2(valor, estado):
    if estado:
        valor += 30
        estado = False
    else:
        valor += 40
        estado = True
    print(f"Resultado {valor}")


def main():
    x = 5
    y = True
    p1 = multiprocessing.Process(target=funcao1, args=(x, y))  # mesmo usando as mesmas variáveis, a passagem de parâmetros se da por cópias
    p2 = multiprocessing.Process(target=funcao2, args=(x, y))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
