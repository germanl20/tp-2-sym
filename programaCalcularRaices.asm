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
    Push dx
    Call RaizCuadrada
    Mov dx, ax
    Pop cx
    Pop bx
    Pop ax
    Neg bx
    Pop bx
    Push bx
    Add bx, dx
    Add ax, ax
    Push ax
    Push dx
    Push ax
    Push bx
    Call Dividir
    Mov cx, ax
    Pop dx
    Pop ax
    Pop bx
    Neg dx
    Pop dx
    Add bx, dx
    Push cx
    Cmp bx, 0
    Jnz UltimaDivisionNegativa
    Push ax
    Push bx
    Call Dividir
    Pop bx
    Ret
UltimaDivisionNegativa:
    Neg bx
    Pop bx
    Push ax
    Push bx
    Call Dividir
    Neg ax
    Pop ax
    Pop bx
    Ret

Entry_point:
    Mov ax, 5
    Mov bx, 10
    Mov cx, 0
    Call CalcularRaices
Fin: