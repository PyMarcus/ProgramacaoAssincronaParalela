# é recomendado compartilhar o minimo de recursos  com threads oara evitar interferencia
# quanto mais recursos forem compartilhados, mais complexo fica o gerenciamento


# recurso de lock => bloqueia recursos para ser usado por uma thread, apenas.
import threading

th = threading.Thread(target=funcao, args=('ola', 10))
lock = th.Lock()
# bloqueio:
lock.acquire()

# ao meio, entre eles, pode-se usar sem interferenica (deve-se usar try e finally)
# ou então, usar um gerenciador de contexto como o with


#desbloqueio
lock.release()

"""é sugerível usar o RLock, pq ele nao bloqueia  a propria thread"""