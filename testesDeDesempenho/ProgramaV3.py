"""
Processamento paralelo é ideal para operações que fazem muito uso de gpu, cpu como
operações em strings, processamento gráfico e algoritmos de busca

Processamento assincrono(nao blocking) é ideal para operações IO
escritas em bancos de dados , consultas a apis etc
"""

import datetime
import asyncio


def main() -> None:
    print("Iniciando processamento de forma assíncrona")
    el = asyncio.get_event_loop()
    inicio = datetime.datetime.now()
    el.run_until_complete(primo(inicio=1, fim=50000))
    final = datetime.datetime.now()
    print(f"Terminou em {(final - inicio)} segundos")


async def primo(inicio: float, fim: float) -> None:
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
    main()  # levou 59 segundos, ou seja, programacao assincronas sao recomendadas para IO mesmo
