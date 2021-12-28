import multiprocessing


def calcular(valor: int) -> int:
    return valor ** 2


def captura_process_name():
    print(f"{multiprocessing.current_process().name}")


def main() -> None:
    tamanho_pool = multiprocessing.cpu_count() * 2 # pega a quantidade de cores e multiplica por 2, para dividir os processos nos cores
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=captura_process_name)  # passa a quantidade de processos a serem gerados, o parâmetro initializer é passado para iniciar funcao toda vez
    print(f"Quantidade de cores a serem usados {tamanho_pool / 2}")
    entradas_funcao = list(range(10))
    print(f"Entradas: {entradas_funcao}")
    resultados = pool.map(calcular, entradas_funcao) # funcao map do multiprocess
    print("Resultado: {}".format(resultados))
    pool.close() # indica que nao vai mapear mais funcoes
    pool.join()  # executa até o fim cada processo


if __name__ == '__main__':
    main()