from instrucciones.instruccion import Instruccion

class Int(Instruccion):
    def __init__(self, nroServicio):
        self.nombre = 'Int'
        self.nroServicio = nroServicio

    def procesar(self, procesador):
        procesoCorrectamente = True
        sistemaOp = procesador.sistema

        if(self.nroServicio == "1"):
            parametros = [procesador.ax, procesador.bx, procesador.cx]
            sistemaOp.syscallHandler(self.nroServicio, parametros)
        else:
            procesador.proceso.error = "Error en instruccion Int: No existe el servicio '" + self.nroServicio + "'"
            procesoCorrectamente = False

        return procesoCorrectamente