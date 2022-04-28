from ensamblador import Ensamblador
from procesador import Procesador
from proceso import Proceso
import os

def main():
    ensamblador = Ensamblador()
    procesador = Procesador()
    ejecutables = list()
    ensamblar = True
    huboErrores = False

    while(ensamblar):
        #Limpia la consola
        os.system("cls")
        print("*******  Ingresa el nombre del archivo a ensamblar o 'x' para no ensamblar mas archivos  *******")
        archivo = input("Ingrese la ruta del archivo a ensamblar: ")

        if(archivo == "x"):
            break

        ejecutable = ensamblador.procesar(archivo)
    
        if(not ensamblador.hayErrores):
            ejecutables.append(ejecutable)
        
        else:
            ensamblar = False
            huboErrores = True

    if(len(ejecutables) > 0 and not huboErrores):
        sistema = Sistema(ejecutables, procesador)
        sistema.ejecutar()
        for proceso in sistema.listaProcesos:
            print("AX FINAL:", proceso.contexto.ax)

class Sistema:
    def __init__(self, ejecutables, procesador):
        self.listaProcesos = list()
        self.procesoActivo = 0
        self.contadorInstrucciones = 0
        self.INSTRUCCIONESMAXIMAS = 5
        self.procesador = procesador

        for ejecutable in ejecutables:
            proceso = Proceso(ejecutable)
            proceso.contexto.ip = proceso.ejecutable.entryPoint
            self.listaProcesos.append(proceso)

        self.procesador.setearSistema(self)
        self.procesador.setearProceso(self.listaProcesos[self.procesoActivo])
    
    def ejecutar(self):
        self.procesador.ejecutar()

    def clockHandler(self):
        self.contadorInstrucciones += 1
        if(self.contadorInstrucciones >= self.INSTRUCCIONESMAXIMAS):
            contexto = self.procesador.obtenerContexto()
            self.listaProcesos[self.procesoActivo].setearContexto(contexto)
            self.listaProcesos[self.procesoActivo].pila = self.procesador.proceso.pila
            self.procesoActivo = self.obtenerProximoProceso()
            self.procesador.setearProceso(self.listaProcesos[self.procesoActivo])
            self.contadorInstrucciones = 0

    
    def obtenerProximoProceso(self):
        procesoActivo = self.procesoActivo
        if(len(self.listaProcesos) > (self.procesoActivo + 1)):
            procesoActivo += 1
        else:
            procesoActivo = 0
        
        return procesoActivo

main()