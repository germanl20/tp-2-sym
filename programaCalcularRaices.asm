Include "programaLibreriaFunciones.asm"

CalcularRaices:
    Push ax
    Push bx
    Push cx
    Push 4
    Push ax
    Call Multiplicar
    Mov dx, ax
    Pop cx
    Push cx
    Push cx
    Push dx
    Call Multiplicar
    Mov dx, ax
    Pop cx
    Pop bx
    Push bx
    Push cx
    Push dx
    Push bx
    Push bx
    Call Multiplicar
    Push ax
    Call Restar
    Mov dx, ax
    
    Pop cx
    Pop bx
    Pop ax
    Ret

Entry_point:
    Mov ax, 5
    Mov bx, 10
    Mov cx, 0
    Call CalcularRaices
Fin: