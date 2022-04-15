from instrucciones.instruccion import Instruccion

class Call(Instruccion):
    def __init__(self, param1, posicionSiguiente):
        self.nombre = 'Call'
        self.param1 = param1
        self.posicionSiguiente = posicionSiguiente

    def procesar(self, procesador):
        procesador.proceso.pila.insert(0, self.posicionSiguiente)
        posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
        procesador.ip = posicion