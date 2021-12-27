import threading
import random
import time
from typing import  List

"""Deve-se usar o with lock em todos os recursos compartilhados pelas threads"""

lock = threading.RLock()
with lock:
    pass
    # executa recurso etc 