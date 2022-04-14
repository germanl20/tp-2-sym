from instrucciones.instruccion import Instruccion

class Push(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Push'
        self.param1 = param1

    def procesar(self, param1):
        if (self.param1 in ["ax", "bx", "cx", "dx"] ):
            self.ejecutable.getPila().append(self.obtenerRegistro(param1))
        else:
            self.ejecutable.pila().append(int(param1))
