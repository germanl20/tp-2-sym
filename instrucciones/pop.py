from instrucciones.instruccion import Instruccion

class Pop(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Pop'
        self.param1 = param1