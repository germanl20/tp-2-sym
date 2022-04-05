from instrucciones.instruccion import Instruccion

class Inc(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Inc'
        self.param1 = param1