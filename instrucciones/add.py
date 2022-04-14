from instrucciones.instruccion import Instruccion

class Add(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Add'
        self.param1 = param1
        self.param2 = param2

    def procesar(self, procesador):
            valueParam1 = procesador.obtenerRegistro(self.param1)
            if(self.param1 in ["ax", "bx", "cx", "dx"] and self.param2 in ["ax", "bx", "cx", "dx"] ):
                valueParam2 =  procesador.obtenerRegistro(self.param2)
                sum = valueParam1 + valueParam2
            else:
                sum = valueParam1 + int(self.param2)

            procesador.setearRegistro(self.param1,sum)