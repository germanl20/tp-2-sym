from instrucciones.instruccion import Instruccion

class Inc(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Inc'
        self.param1 = param1

    def procesar(self, procesador):
        valueParam1 = procesador.obtenerRegistro(self.param1)
        procesador.setearRegistro(self.param1, int(valueParam1) + 1)
