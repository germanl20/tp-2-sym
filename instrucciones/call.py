from instrucciones.instruccion import Instruccion

class Call(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Call'
        self.param1 = param1