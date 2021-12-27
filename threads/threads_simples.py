import threading  # step1
import time


def main():
    th = threading.Thread(target=conte, args=('Ovelha', 10))  # threading recebe target(a funcao), args (argumentos da funcao) # step2
    print("Executa outras coisas, enquanto a thread executa")
    th.start()  # adiciona a thread na pool de threads do sistema operacional para execução (não executa) # step3
    for n in range(20):
        print(n)
    th.join()  # aguarda aqui, enquanto a thread nao termina # step4
    print("Pronto!Daqui para baixo pode ser executado")


def conte(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    print(threading.Thread.__mro__)

# aqui, então, foi executado duas threads.A principal para rodar o python e a criada