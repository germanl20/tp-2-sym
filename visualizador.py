import curses
import time

class Visualizador:

    def __init__(self):
        self.pantalla = curses.initscr()

    def mostrar(self, ejecutable, procesador):
        try:
            self.pantalla.clear()
            
            totalMostrado = 0

            #Si "ip" vale 0 o 1
            if(procesador.ip <= 1):
                for indice in range(len(ejecutable.listaInstruccionesCodFuente)):
                    #Si es la instruccion ejecutada, muestro con una flecha
                    if(indice == procesador.ip):
                        self.pantalla.addstr(indice, 0, "->")
                        self.pantalla.addstr(indice, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())
                    else:
                        self.pantalla.addstr(indice, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())
                    
                    totalMostrado += 1
                    if(totalMostrado == 5):
                        if(totalMostrado != len(ejecutable.listaInstruccionesCodFuente)):
                            self.pantalla.addstr(indice + 1, 3, "...")
                        break
            
            #Si estoy en las ultimas 2 posiciones
            elif(procesador.ip + 1 >= (len(ejecutable.listaInstruccionesCodFuente) - 1)):
                rango = range(len(ejecutable.listaInstruccionesCodFuente))
                if(len(rango) > 5):
                    rango = rango[len(rango) - 5: len(rango)]
                    self.pantalla.addstr(0, 3, "...")
                    totalMostrado += 1

                for indice in rango:
                    #Si es la instruccion ejecutada, muestro con una flecha
                    if(indice == procesador.ip):
                        self.pantalla.addstr(totalMostrado, 0, "->")
                        self.pantalla.addstr(totalMostrado, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())
                    else:
                        self.pantalla.addstr(totalMostrado, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())
                    
                    totalMostrado += 1
            
            #Si esta en el medio de la lista
            else:
                indice = 0
                if(procesador.ip - 2 > 0):
                    self.pantalla.addstr(indice, 3, "...")
                    indice += 1

                self.pantalla.addstr(indice, 3, ejecutable.listaInstruccionesCodFuente[procesador.ip - 2].strip())
                self.pantalla.addstr(indice + 1, 3, ejecutable.listaInstruccionesCodFuente[procesador.ip - 1].strip())

                self.pantalla.addstr(indice + 2, 0, "->")
                self.pantalla.addstr(indice + 2, 3, ejecutable.listaInstruccionesCodFuente[procesador.ip].strip())

                self.pantalla.addstr(indice + 3, 3, ejecutable.listaInstruccionesCodFuente[procesador.ip + 1].strip())
                self.pantalla.addstr(indice + 4, 3, ejecutable.listaInstruccionesCodFuente[procesador.ip + 2].strip())

                self.pantalla.addstr(indice + 5, 3, "...")


            #Mostramos los registros del procesador
            self.pantalla.addstr(0, 25, "ax: " + str(procesador.ax))
            self.pantalla.addstr(1, 25, "bx: " + str(procesador.bx))
            self.pantalla.addstr(2, 25, "cx: " + str(procesador.cx))
            self.pantalla.addstr(3, 25, "dx: " + str(procesador.dx))
            self.pantalla.addstr(4, 25, "ip: " + str(procesador.ip))
            self.pantalla.addstr(5, 25, "flag: " + str(procesador.flag))


            #Mostramos la memoria de video del proceso
            self.pantalla.addstr(0, 40, "--Memoria de Video--")
            for fila in range(len(procesador.proceso.memoriaVideo)):
                filaImprimir = fila + 1
                for columna in range(len(procesador.proceso.memoriaVideo[fila])):
                    columnaImprimir = columna + 40
                    self.pantalla.addstr(filaImprimir, columnaImprimir, str(procesador.proceso.memoriaVideo[fila][columna]))

            self.pantalla.refresh()

            time.sleep(0.5)
        except:
            pass

    def mostrarFin(self, listaProcesos):
        print("\n\n", "¡Termino la ejecucion!")
        print("Los procesos terminaron con los siguientes valores: ", end="\n\n")

        for proceso in listaProcesos:
            if(proceso.error == ""):
                print("AX:", proceso.contexto.ax)
                print("BX:", proceso.contexto.bx)
                print("CX:", proceso.contexto.cx)
                print("DX:", proceso.contexto.dx)
                print("IP:", proceso.contexto.ip)
                print("FLAG:", proceso.contexto.flag)
                
            else:
                print("ERROR:", proceso.error)
            print("----------------", end='\n\n')