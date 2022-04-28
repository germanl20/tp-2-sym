from enum import Enum

from contexto import Contexto


class Proceso:
    def __init__(self, ejecutable):
        self.ejecutable = ejecutable
        self.pila = list()
        self.estado = ProcesoEstado.BLOQUEADO
        self.contexto = Contexto()

    def setearContexto(self, contexto):
        self.contexto = contexto


class ProcesoEstado(Enum):
    BLOQUEADO = 0,
    EJECUTANDO = 1,
    FINALIZADO = 2