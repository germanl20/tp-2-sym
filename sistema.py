from ensamblador import Ensamblador
from procesador import Procesador, ProcesadorEstado
from proceso import Proceso, ProcesoEstado
from visualizador import Visualizador
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

class Sistema:
    def __init__(self, ejecutables, procesador):
        self.listaProcesos = list()
        self.procesoActivo = 0
        self.contadorInstrucciones = 0
        self.INSTRUCCIONESMAXIMAS = 5
        self.procesador = procesador
        self.visualizador = Visualizador()

        for ejecutable in ejecutables:
            proceso = Proceso(ejecutable)
            proceso.contexto.ip = proceso.ejecutable.entryPoint
            self.listaProcesos.append(proceso)

        self.procesador.setearSistema(self)
        self.listaProcesos[self.procesoActivo].estado = ProcesoEstado.EJECUTANDO
        self.procesador.setearProceso(self.listaProcesos[self.procesoActivo])
        self.procesador.setearVisualizador(self.visualizador)
    
    def ejecutar(self):
        self.procesador.ejecutar()
        self.visualizador.mostrarFin(self.listaProcesos)

    def clockHandler(self):
        self.contadorInstrucciones += 1
        if(self.contadorInstrucciones >= self.INSTRUCCIONESMAXIMAS):
            self.cambiarProceso()

    def cambiarProceso(self):
        contexto = self.procesador.obtenerContexto()
        self.listaProcesos[self.procesoActivo].setearContexto(contexto)

        #Si hubo error, finalizo el proceso
        if(self.listaProcesos[self.procesoActivo].error != ""):
            self.listaProcesos[self.procesoActivo].estado = ProcesoEstado.FINALIZADO

        elif(len(self.listaProcesos[self.procesoActivo].ejecutable.listaInstrucciones) == self.listaProcesos[self.procesoActivo].contexto.ip):
            self.listaProcesos[self.procesoActivo].estado = ProcesoEstado.FINALIZADO
            
        elif(self.listaProcesos[self.procesoActivo].estado == ProcesoEstado.EJECUTANDO):
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
                procesoActivo += 1
                if(len(self.listaProcesos) > procesoActivo):
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

    def syscallHandler(self, nroServicio, parametros):
        #Imprimir por pantalla
        if(nroServicio == "1"):
            numero = parametros[0]
            fila = parametros[1]
            columna = parametros[2]
            self.listaProcesos[self.procesoActivo].memoriaVideo[fila][columna] = numero

main()