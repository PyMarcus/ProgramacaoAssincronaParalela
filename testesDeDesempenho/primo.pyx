import cython



def primo(inicio: cython.int, fim: cython.int):
    contador: cython.int = 0
    n: cython.int = 1
    with nogil:  
        while inicio < fim:
            while n < inicio:
                if inicio % n == 0:
                    contador += 1
                n += 1
            if contador < 2:
                pass
            contador = 0
            n = 1
            inicio += 1
