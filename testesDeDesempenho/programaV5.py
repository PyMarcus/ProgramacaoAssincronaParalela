# ultima versão do programa implementando cython
from datetime import datetime
from primo import primo


def main() -> None:
    a = datetime.now()
    primo(1, 50000)
    b = datetime.now()
    print(f"Executou em {b - a} segundos")


if __name__ == '__main__':
    main()  # so compilando para linguagem de máquina, demorou 34segundos, em Cython, 0.00.00.32 segundos (SUPER RÁPIDO)
  