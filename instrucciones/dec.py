from instrucciones.instruccion import Instruccion

class Dec(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Dec'
        self.param1 = param1