from instrucciones.instruccion import Instruccion

class Cmp(Instruccion):
    def __init__(self, param1, param2):
        self.nombre = 'Cmp'
        self.param1 = param1
        self.param2 = param2

    def procesar(self, procesador):
        valueParam1 = procesador.obtenerRegistro(self.param1)
        if(self.param1 in ["ax", "bx", "cx", "dx"] and self.param2 in ["ax", "bx", "cx", "dx"] ):
            valueParam2 =  procesador.obtenerRegistro(self.param2)
            if (valueParam1 == valueParam2):
                procesador.setearRegistro(self.flag, 0)
            else:
                procesador.setearRegistro(self.flag, 1)
        else: 
            if(self.param1 in ["ax", "bx", "cx", "dx"] and self.param2 not in ["ax", "bx", "cx", "dx"] ):
                if(self.param1 == self.param2):
                    procesador.setearRegistro(self.flag, 0)
                else:
                    procesador.setearRegistro(self.flag, 1)

## Validar