from instrucciones.instruccion import Instruccion

class Push(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Push'
        self.param1 = param1