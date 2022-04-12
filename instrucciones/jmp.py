from instrucciones.instruccion import Instruccion

class Jmp(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Jmp'
        self.param1 = param1

    def procesar(self, procesador):
        posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
        procesador.ip = posicion