from instrucciones.instruccion import Instruccion

class Jmp(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Jmp'
        self.param1 = param1

    def procesar(self, procesador):
        procesoCorrectamente = True

        if(self.param1 not in procesador.proceso.ejecutable.lookupTable):
            print("Error en instruccion Jmp: No existe la etiqueta '" + self.param1 + "'")
            procesoCorrectamente = False
        else:
            posicion = procesador.proceso.ejecutable.lookupTable[self.param1]
            procesador.ip = posicion
    
        return procesoCorrectamente