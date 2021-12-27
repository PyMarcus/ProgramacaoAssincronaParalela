# primeira versão do programa para medir o desempenho de execução
# o python, normalmente, é lento, pois ele possui um mecanismo de bloquei chamado GIL (Global interpreter Lock)
# isso impede que ele use várias threads limitando a velocidade de execução, por questões de memória e segurança
# no entanto, com programação concorrente (uso de várias cores), pode-se com a programação paralela ( quebrar a tarefa
# e executá-la em cores diferentes ) ou com programação assíncrona (executar parte do código em uma thread e quando
# for executado, pegar a resposta (call back)e enviar a thread principal), pode-se deixar os scripts mais velozes.
import datetime


# python padrão
def main():
    final = 50000
    inicio = 1
    tempo0 = datetime.datetime.now()
    primo(inicio, final)
    tempo1 = datetime.datetime.now()
    print(f"Levou {(tempo1 - tempo0).total_seconds():.2f} segundos")


def primo(inicio, fim):
    primos = []
    contador = 0
    numeros = [numero for numero in range(inicio, fim + 1)]
    for numero in numeros:
        for n in range(1, numero + 1):
            if numero % n == 0:
                contador += 1
        if contador <= 2:
            primos.append(numero)
        contador = 0
    print(primos)


if __name__ == '__main__':
    main() # resposta 57.26 segundos com alguns programas abertos no pc