from instrucciones.instruccion import Instruccion

class Ret(Instruccion):
    def __init__(self):
        self.nombre = 'Ret'

    def procesar(self, procesador):
        procesoCorrectamente = True

        valor = procesador.proceso.pila[0]
        procesador.ip = valor
        procesador.proceso.pila.pop(0)

        return procesoCorrectamente