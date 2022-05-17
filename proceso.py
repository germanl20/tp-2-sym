from enum import Enum
import numpy as np

from contexto import Contexto


class Proceso:
    def __init__(self, ejecutable):
        self.ejecutable = ejecutable
        self.pila = list()
        self.estado = ProcesoEstado.BLOQUEADO
        self.contexto = Contexto()
        self.error = ""
        self.memoriaVideo = np.zeros((10, 10), dtype=int)

    def setearContexto(self, contexto):
        self.contexto = contexto


class ProcesoEstado(Enum):
    BLOQUEADO = 0,
    EJECUTANDO = 1,
    FINALIZADO = 2