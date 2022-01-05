# terceira versão do programa para medir o desempenho de execução
# o python, normalmente, é lento, pois ele possui um mecanismo de bloquei chamado GIL (Global interpreter Lock)
# isso impede que ele use várias threads limitando a velocidade de execução, por questões de memória e segurança
# no entanto, com programação concorrente (uso de várias cores), pode-se com a programação paralela ( quebrar a tarefa
# e executá-la em cores diferentes ) ou com programação assíncrona (executar parte do código em uma thread e quando
# for executado, pegar a resposta (call back)e enviar a thread principal), pode-se deixar os scripts mais velozes.
import datetime
from multiprocessing import Process
import multiprocessing


# python padrão
def main() -> None:
    qnt_cores: int = multiprocessing.cpu_count()  # conta quantos cores tem o processador
    final: int = 50000
    threads: list = []
    tempo0: datetime = datetime.datetime.now()
    # usando cada core pra processar uma parte

    pc = [Process(target=primo, kwargs={'inicio': 1, 'fim': 10000},
                              daemon=True),
          Process(target=primo, kwargs={'inicio': 10000, 'fim': 20000},
                 daemon=True),
          Process(target=primo, kwargs={'inicio': 20000, 'fim': 30000},
                 daemon=True),
          Process(target=primo, kwargs={'inicio': 40000, 'fim': 50000},
                              daemon=True),

          ]  # daemon faz mesmo que o processo pai morra, os filhos continuem
    [tt.start() for tt in pc]
    [tt.join() for tt in pc]
    tempo1: datetime = datetime.datetime.now()
    print(f"Levou {(tempo1 - tempo0).total_seconds():.2f} segundos")


def primo(inicio: float, fim: float) -> None:
    primos: list = []
    contador: int = 0
    numeros: list = [numero for numero in range(int(inicio), int(fim) + 1)]
    for numero in numeros:
        for n in range(1, numero + 1):
            if numero % n == 0:
                contador += 1
        if contador <= 2:
            primos.append(numero)
        contador: int = 0
    print(primos)


if __name__ == '__main__':
    main()  # Levou 21.05 segundos
