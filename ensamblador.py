import re

from ejecutable import Ejecutable
from instrucciones.add import Add
from instrucciones.cmp import Cmp
from instrucciones.dec import Dec
from instrucciones.etiqueta import Etiqueta
from instrucciones.inc import Inc
from instrucciones.jmp import Jmp
from instrucciones.jnz import Jnz
from instrucciones.mov import Mov

class Ensamblador:

    def __init__(self):
        self.ejecutable = Ejecutable()
        self.listaErrores = dict()
    
    
    def procesar(self, nombreArchivo):
        archivo = open(nombreArchivo)
        numeroDeLinea = 0

        for linea in archivo:
            numeroDeLinea += 1
            #Paso la linea a minuscula
            linea = linea.lower()
            
            self.__procesarLineaArchivo(linea, numeroDeLinea)

        if(len(self.listaErrores) > 0):
           self.__mostrarErrores()
        
        else:
            self.__mostrarEjecutableGenerado()


    def __procesarLineaArchivo(self, linea, numeroDeLinea):
        match = re.search('^\s*([\w_]+):\s*$', linea)
        #Si es una etiqueta
        if(match):
            etiqueta = match.group(1)
            
            if(etiqueta == 'entry_point'):
                if(self.ejecutable.entryPoint == ""):
                    self.ejecutable.entryPoint = numeroDeLinea
                    self.ejecutable.listaInstrucciones.append(Etiqueta())
                    self.ejecutable.listaInstruccionesCodFuente.append(linea)
                
                #Si entryPoint no es vacio quiere decir que hay mas de uno en el codigo fuente
                else:
                    self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": No puede haber mas de un entry_point"

            else:
                if(etiqueta not in self.ejecutable.lookupTable):
                    self.ejecutable.lookupTable[etiqueta] = numeroDeLinea
                    self.ejecutable.listaInstrucciones.append(Etiqueta())
                    self.ejecutable.listaInstruccionesCodFuente.append(linea)
                else:
                    self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": Etiqueta duplicada"
        
        #Sino tendria que ser una instruccion
        else:
            self.__procesarInstruccion(linea, numeroDeLinea)

    
    def __procesarInstruccion(self, linea, numeroDeLinea):
        match = re.search('^\s*(mov|add|cmp|inc|dec|jmp|jnz)\s+(.*)', linea)
        
        if (match):
            instruccion = match.group(1)
            parametros = match.group(2)

            #Si es una instruccion que lleve dos parametros
            if(instruccion == 'mov' or instruccion == 'add' or instruccion == 'cmp'):
                #Obtengo los parametros
                #match = re.search('^(\w+)\s*,\s*(\w+)\s*$', parametros)
                match = re.search('^(ax|bx|cx|dx)\s*,\s*(ax|bx|cx|dx|\d+)\s*$', parametros)
                if (match):
                    if(instruccion == 'mov'):
                        instruccionNueva = Mov(match.group(1), match.group(2))
                    
                    elif(instruccion == 'add'):
                        instruccionNueva = Add(match.group(1), match.group(2))

                    elif(instruccion == 'cmp'):
                        instruccionNueva = Cmp(match.group(1), match.group(2))
                    
                    self.ejecutable.listaInstrucciones.append(instruccionNueva)
                    self.ejecutable.listaInstruccionesCodFuente.append(linea)
                
                #Si dio error por parametros invalidos
                else:
                    self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": Parametros no validos"
            
            elif(instruccion == 'jmp' or instruccion == 'jnz'):
                #Obtengo los parametros
                match = re.search('^(\w+)\s*$', parametros)
                if(match):
                    if(instruccion == 'jmp'):
                        instruccionNueva = Jmp(match.group(1))
                    
                    elif(instruccion == 'jnz'):
                        instruccionNueva = Jnz(match.group(1))
                    
                    self.ejecutable.listaInstrucciones.append(instruccionNueva)
                    self.ejecutable.listaInstruccionesCodFuente.append(linea)
                
                else:
                    self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": Parametro no valido - Debe ser una sola palabra que represente el nombre de una etiqueta"
            
            else:
                #Obtengo los parametros
                match = re.search('^(ax|bx|cx|dx)\s*$', parametros)
                if(match):
                    if(instruccion == 'inc'):
                        instruccionNueva = Inc(match.group(1))
                    
                    elif(instruccion == 'dec'):
                        instruccionNueva = Dec(match.group(1))
                    
                    self.ejecutable.listaInstrucciones.append(instruccionNueva)
                    self.ejecutable.listaInstruccionesCodFuente.append(linea)
                
                else:
                    self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": Parametro no valido - Debe ser 'ax', 'bx', 'cx' o 'dx'"
        
        #Si dio error por instruccion mal escrita o no valida
        else:
            self.listaErrores[numeroDeLinea] = "Error en la linea " + str(numeroDeLinea) + ": instruccion no valida"

    
    def __mostrarErrores(self):
        for error in self.listaErrores:
            print(self.listaErrores[error])


    def __mostrarEjecutableGenerado(self):
        #Imprimo el entry_point
        print("\n", "Entry_Point:", self.ejecutable.entryPoint)

        #Imprimo por consola lo que generamos:
        print("\n", "Instrucciones generadas:")
        for instruccion in self.ejecutable.listaInstrucciones:
            print(instruccion)

        #Imprimo el diccionario lookupTable:
        print("\n", "Diccionario lookupTable:")
        for etiqueta in self.ejecutable.lookupTable:
            print("Etiqueta:", etiqueta, "- Posicion:", self.ejecutable.lookupTable[etiqueta])
                


en = Ensamblador()
archivo = input("Ingrese la ruta del archivo a ensamblar: ")
en.procesar(archivo)