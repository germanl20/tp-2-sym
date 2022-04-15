from instrucciones.instruccion import Instruccion

class Pop(Instruccion):
    def __init__(self, param1):
        self.nombre = 'Pop'
        self.param1 = param1

    def procesar(self, procesador):
        valor = procesador.proceso.pila[0]
        procesador.setearRegistro(self.param1, int(valor))
        procesador.proceso.pila.pop(0)