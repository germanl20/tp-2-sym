import curses
import time

class Visualizador:

    def __init__(self):
        self.pantalla = curses.initscr()

    def mostrar(self, ejecutable, procesador):
        try:
            self.pantalla.clear()

            for indice in range(len(ejecutable.listaInstruccionesCodFuente)):
                #Si es la instruccion ejecutada, muestro con una flecha
                if(indice == procesador.ip):
                    self.pantalla.addstr(indice, 0, "->")
                    self.pantalla.addstr(indice, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())
                else:
                    self.pantalla.addstr(indice, 3, ejecutable.listaInstruccionesCodFuente[indice].strip())


            #Mostramos los registros del procesador
            self.pantalla.addstr(0, 25, "ax: " + str(procesador.ax))
            self.pantalla.addstr(1, 25, "bx: " + str(procesador.bx))
            self.pantalla.addstr(2, 25, "cx: " + str(procesador.cx))
            self.pantalla.addstr(3, 25, "dx: " + str(procesador.dx))
            self.pantalla.addstr(4, 25, "ip: " + str(procesador.ip))
            self.pantalla.addstr(5, 25, "flag: " + str(procesador.flag))
            self.pantalla.refresh()

            time.sleep(0.3)
        except:
            pass