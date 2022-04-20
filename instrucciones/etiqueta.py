from instrucciones.instruccion import Instruccion

# Esta instruccion no debe hacer nada, solo representa una etiqueta
class Etiqueta(Instruccion):
    def __init__(self):
        self.nombre = 'Etiqueta'

    def procesar(self, procesador):
        return True