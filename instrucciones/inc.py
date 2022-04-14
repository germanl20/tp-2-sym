from instrucciones.instruccion import Instruccion

class Inc(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Inc'
        self.param1 = param1

    def procesar(self, procesador):
        if(self.param1 in ["ax", "bx", "cx", "dx"]):
                valuepParam1 = procesador.obtenerRegistro(self.param1)
                procesador.setearRegistro(valuepParam1 + 1)
