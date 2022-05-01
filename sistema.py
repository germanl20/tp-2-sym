from ensamblador import Ensamblador
from procesador import Procesador, ProcesadorEstado
from proceso import Proceso, ProcesoEstado
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
            print("AX:", proceso.contexto.ax)
            print("BX:", proceso.contexto.bx)
            print("CX:", proceso.contexto.cx)
            print("DX:", proceso.contexto.dx)
            print("IP:", proceso.contexto.ip)
            print("FLAG:", proceso.contexto.flag)
            print("----------------", end='\n\n')

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
            self.cambiarProceso()

    def cambiarProceso(self):
        contexto = self.procesador.obtenerContexto()
        self.listaProcesos[self.procesoActivo].setearContexto(contexto)
        self.listaProcesos[self.procesoActivo].pila = self.procesador.proceso.pila
        self.listaProcesos[self.procesoActivo].error = self.procesador.proceso.error
        self.listaProcesos[self.procesoActivo].estado = self.procesador.proceso.estado
        if(self.listaProcesos[self.procesoActivo].estado == ProcesoEstado.EJECUTANDO):
            self.listaProcesos[self.procesoActivo].estado = ProcesoEstado.BLOQUEADO
        
        self.procesoActivo = self.obtenerProximoProceso()

        if(self.procesoActivo != -1):
            self.listaProcesos[self.procesoActivo].estado = ProcesoEstado.EJECUTANDO
            self.procesador.setearProceso(self.listaProcesos[self.procesoActivo])
            self.contadorInstrucciones = 0
        else:
            self.procesador.estado = ProcesadorEstado.INACTIVO

    
    def obtenerProximoProceso(self):
        procesoActivo = self.procesoActivo

        #Si hay procesos que ejecutar
        if(self.hayProcesosBloqueados()):
            seguirBuscando = True
            while(seguirBuscando):
                if(len(self.listaProcesos) > (self.procesoActivo + 1)):
                    procesoActivo += 1
                    if(self.listaProcesos[procesoActivo].estado == ProcesoEstado.BLOQUEADO):
                        seguirBuscando = False
                else:
                    procesoActivo = 0
                    if(self.listaProcesos[procesoActivo].estado == ProcesoEstado.BLOQUEADO):
                        seguirBuscando = False
        else:
            procesoActivo = -1
        
        return procesoActivo

    def hayProcesosBloqueados(self):
        hayProcesosBloqueados = False
        for proceso in self.listaProcesos:
            if(proceso.estado == ProcesoEstado.BLOQUEADO):
                hayProcesosBloqueados = True
                break
        
        return hayProcesosBloqueados

main()