class Procesador:
    def __init__(self):
        self.ax
        self.bx
        self.cx
        self.dx
        self.ip
        self.flag
        self.proceso

    def ejecutar(self, proceso):
        self.proceso = proceso

        # ip = proceso.ejecutable.entry_point
        # for ip; ip < proceso.ejecutable.listaInstrucciones.lenght; ip++:
        #   ejecutable.listaInstruccion[ip].procesar(self)

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