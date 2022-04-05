from instrucciones.instruccion import Instruccion

class Mov(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Mov'
        self.param1 = param1
        self.param2 = param2