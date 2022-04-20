from instrucciones.instruccion import Instruccion

class Call(Instruccion):
    def __init__(self, param1, posicionSiguiente):
        self.nombre = 'Call'
        self.param1 = param1
        self.posicionSiguiente = posicionSiguiente

    def procesar(self, procesador):
        procesoCorrectamente = True

        procesador.proceso.pila.insert(0, self.posicionSiguiente)
        if(self.param1 not in procesador.proceso.ejecutable.lookupTable):
            print("Error en instruccion Call: No existe la etiqueta '" + self.param1 + "'")
            procesoCorrectamente = False
        else:
            posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
            procesador.ip = posicion

        return procesoCorrectamente