# api de multiprocessamento do python
import multiprocessing


# pegar nome do processo que foi gerado
print(f"Processo gerado: {multiprocessing.current_process().name}")


def faz_algo(algo):
    print(f"Fazendo {algo}")


def main():
    process = multiprocessing.Process(target=faz_algo, args=("Nada",))
    print(f"Iniciando processo com o nome: {process.name}")
    process.start()
    process.join()


if __name__ == '__main__':
    main()
