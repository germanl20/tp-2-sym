from ejecutable import Ejecutable
from instrucciones.mov import Mov

class Ensamblador:

    def __init__(self):
        self.ejecutable = Ejecutable()
    
    
    def procesar(self, nombreArchivo):
        archivo = open(nombreArchivo)
        numeroDeLinea = 0

        for linea in archivo:
            numeroDeLinea += 1
            #Paso la linea a minuscula
            linea = linea.lower()
            
            procesoBien = self.__procesarLineaArchivo(linea, numeroDeLinea)
            if(not procesoBien): break

    
    def __procesarLineaArchivo(self, linea, numeroDeLinea) -> bool:
        procesoBien = True;

        if 'mov ' in linea:
            procesoBien = self.__procesarMov(linea, numeroDeLinea)
        
        elif 'inc ' in linea:
            #FALTA - CREO INSTANCIA DE INC Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('inc', linea)

        elif 'dec ' in linea:
            #FALTA - CREO INSTANCIA DE DEC Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('dec', linea)
    
        elif 'cmp ' in linea:
            #FALTA - CREO INSTANCIA DE CMP Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('cmp', linea)
        
        elif 'add ' in linea:
            #FALTA - CREO INSTANCIA DE ADD Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('add', linea)
        
        elif 'jmp ' in linea:
            #FALTA - CREO INSTANCIA DE JMP Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('jmp', linea)
       
        elif 'jnz ' in linea:
            #FALTA - CREO INSTANCIA DE JMP Y LA AGREGO A LA LISTA DEL EJECUTABLE
            print('jnz', linea)

        elif 'entry_point:' in linea:
            #FALTA - GUARDO EL NUMERO DE LA SIGUIENTE LINEA EN LA VARIABLE entryPoint de la clase Ejecutable
            print('entry_point', linea)
            
        else:
            #FALTA - Analizo si se trata de una etiqueta o un error
            print('else', linea)
        
        return procesoBien

    
    def __imprimirErrorEnLinea(self, numeroDeLinea):
        print("Error en la linea", numeroDeLinea)


    def __procesarMov(self, linea, numeroDeLinea) -> bool:
        procesoBien = True;

        try:
            lineaSplit = linea.split()

            #Le sacamos la coma al primer registro
            param1 = lineaSplit[1].split(",")
            param1 = "".join(param1)

            param2 = lineaSplit[2]

            #Validamos los params
            if(("ax" == param1 or "bx" == param1 or "cx" == param1 or "dx" == param1)
                and ("ax" == param2 or "bx" == param2 or "cx" == param2 or "dx" == param2 or param2.isnumeric())):
                
                mov = Mov(param1, param2)
                self.ejecutable.listaInstrucciones.append(mov)
                self.ejecutable.listaInstruccionesCodFuente.append(linea)
            else:
                #Es invalido
                procesoBien = False
                self.__imprimirErrorEnLinea(numeroDeLinea)

        except Exception as e:
            procesoBien = False
            self.__imprimirErrorEnLinea(numeroDeLinea)
        
        return procesoBien


en = Ensamblador()
en.procesar("codigoAssembler.asm")