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
        # self.memoriaVideo = np.zeros((10, 10), dtype=int)
        self.memoriaVideo = []
        self.__inicializarMemoriaVideo()
        

    def setearContexto(self, contexto):
        self.contexto = contexto

    def __inicializarMemoriaVideo(self):
        for i in range(10):
            self.memoriaVideo.append([])
            for j in range(10):
                self.memoriaVideo[i].append('-')


class ProcesoEstado(Enum):
    BLOQUEADO = 0,
    EJECUTANDO = 1,
    FINALIZADO = 2