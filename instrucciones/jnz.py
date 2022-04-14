from instrucciones.instruccion import Instruccion

class Jnz(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Jnz'
        self.param1 = param1

    def procesar(self, procesador):
        if procesador.obtenerRegistro(self.flag):
            posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
            procesador.ip = posicion
        else:
            procesador.ip + 1


## Revisar que esté ok el uso del flag y el incremento de la posición en caso de que el flag no sea true