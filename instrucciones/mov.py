from instrucciones.instruccion import Instruccion

class Mov(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Mov'
        self.param1 = param1
        self.param2 = param2

    def procesar(self, procesador):
            if(self.param2 in ["ax", "bx", "cx", "dx"]):
                procesador.setearRegistro(self.param1, procesador.obtenerRegistro(self.param2))
            else:
                procesador.setearRegistro(self.param1, int(self.param2))