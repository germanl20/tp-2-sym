from instrucciones.instruccion import Instruccion

class Push(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Push'
        self.param1 = param1

    def procesar(self, procesador):
        procesoCorrectamente = True

        valueParam1 = self.param1

        if (self.param1 in ["ax", "bx", "cx", "dx"]):
            valueParam1 = procesador.obtenerRegistro(self.param1)
        
        procesador.proceso.pila.insert(0, valueParam1)

        return procesoCorrectamente
