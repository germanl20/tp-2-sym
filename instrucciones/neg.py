from instrucciones.instruccion import Instruccion

class Neg(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Neg'
        self.param1 = param1

    def procesar(self, procesador):
        procesoCorrectamente = True
        numero = self.param1

        if(self.param1 in ["ax", "bx", "cx", "dx"]):
            numero = procesador.obtenerRegistro(self.param1)
        
        numero = int(numero) * -1
        procesador.proceso.pila.insert(0, numero)

        return procesoCorrectamente