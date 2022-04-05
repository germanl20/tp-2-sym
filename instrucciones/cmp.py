from instrucciones.instruccion import Instruccion

class Cmp(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Cmp'
        self.param1 = param1
        self.param2 = param2