from contexto import Contexto
from instrucciones.ret import Ret
from enum import Enum

from proceso import ProcesoEstado

class Procesador:
    def __init__(self):
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0
        self.ip = 0
        self.flag = 0
        self.estado = ProcesadorEstado.ACTIVO


    def ejecutar(self):
        print("\n\n", "*** Ejecucion del programa ***")

        while(self.estado == ProcesadorEstado.ACTIVO):
            procesoCorrectamente = True
            while (self.ip < len(self.proceso.ejecutable.listaInstrucciones) and procesoCorrectamente):
                instruccion = self.proceso.ejecutable.listaInstrucciones[self.ip]
                procesoCorrectamente = instruccion.procesar(self)

                if(procesoCorrectamente):
                    #Cuando es Ret no se incrementa porque Ret ya modifica el ip y no va a una etiqueta
                    if(not isinstance(instruccion, Ret)):
                        self.ip = self.ip + 1
                    
                    #Llamamos al sistema operativo para evaluar si hay que pasar a otro proceso
                    self.clockHandler()
            
            #Si termino el ejecutable
            self.proceso.estado = ProcesoEstado.FINALIZADO
            self.sistema.cambiarProceso()


    def setearRegistro(self, registro, valor):
        match registro:
            case "ax": 
                self.ax = valor
            case "bx": 
                self.bx = valor
            case "cx": 
                self.cx = valor
            case "dx": 
                self.dx = valor
            case "flag": 
                self.flag = valor    


    def obtenerRegistro(self, registro):
        match registro:
            case "ax": 
                return self.ax
            case "bx": 
                return self.bx
            case "cx": 
                return self.cx
            case "dx": 
                return self.dx
            case "flag": 
                return self.flag


    def setearSistema(self, sistema):
        self.sistema = sistema

    def setearProceso(self, proceso):
        self.proceso = proceso
        self.setearContexto(proceso.contexto)
    
    def setearContexto(self, contexto):
        self.ax = contexto.ax
        self.bx = contexto.bx
        self.cx = contexto.cx
        self.dx = contexto.dx
        self.ip = contexto.ip
        self.flag = contexto.flag

    def obtenerContexto(self):
        contexto = Contexto()
        contexto.ax = self.ax
        contexto.bx = self.bx
        contexto.cx = self.cx
        contexto.dx = self.dx
        contexto.ip = self.ip
        contexto.flag = self.flag

        return contexto


    def clockHandler(self):
        self.sistema.clockHandler()


class ProcesadorEstado(Enum):
    ACTIVO = 0,
    INACTIVO = 1