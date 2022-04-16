from instrucciones.instruccion import Instruccion

class Jnz(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Jnz'
        self.param1 = param1

    def procesar(self, procesador):
        if procesador.flag == 1:
            posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
            procesador.ip = posicion