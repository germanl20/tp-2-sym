from instrucciones.instruccion import Instruccion

class Jnz(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Jnz'
        self.param1 = param1