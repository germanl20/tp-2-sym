from instrucciones.ret import Ret


class Procesador:
    def __init__(self):
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0
        self.ip = 0
        self.flag = 0


    def ejecutar(self, proceso):
        self.proceso = proceso
        self.ip = self.proceso.ejecutable.entryPoint
        instrucciones = self.proceso.ejecutable.listaInstrucciones

        while self.ip < len(instrucciones):
            instruccion = instrucciones[self.ip]
            instruccion.procesar(self)

            #Cuando es Ret no se incrementa porque Ret ya modifica el ip y no va a una etiqueta
            if(not isinstance(instruccion, Ret)):
                self.ip = self.ip + 1
        
        print("\n\n", "Ejecucion del programa - Los registros terminaron con los valores:")
        print("ax", self.ax)
        print("bx", self.bx)
        print("cx", self.cx)
        print("dx", self.dx)
        print("flag", self.flag)


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