from instrucciones.instruccion import Instruccion

class Cmp(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Cmp'
        self.param1 = param1
        self.param2 = param2

    def procesar(self, procesador):
        procesoCorrectamente = True

        valueParam1 = procesador.obtenerRegistro(self.param1)
        valueParam2 = self.param2

        if(self.param2 in ["ax", "bx", "cx", "dx"]):
            valueParam2 = procesador.obtenerRegistro(self.param2)

        if (valueParam1 == int(valueParam2)):
            procesador.flag = 0
        else:
            procesador.flag = 1

        return procesoCorrectamente