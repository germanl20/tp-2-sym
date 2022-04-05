from instrucciones.instruccion import Instruccion

class Add(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Add'
        self.param1 = param1
        self.param2 = param2