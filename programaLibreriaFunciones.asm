Restar:
    Pop ax
    Pop bx
    Pop cx
    Push ax
    Neg cx
    Pop cx
    Add bx, cx
    Mov ax, bx
    Ret

Multiplicar:
    Pop cx
    Pop ax
    Pop bx
    Push cx
    Mov cx, 1
    Mov dx, 0
CicloMultiplicar:
    Add dx, ax
    Cmp cx, bx
    Inc cx
    Jnz CicloMultiplicar
    Mov ax, dx
    Ret

Entry_point:
    Push 2
    Push 14
    Call Restar
    Mov bx, 0
    Mov cx, 0
    Int 1

    Push 3
    Push 2
    Call Multiplicar
    Mov bx, 1
    Mov cx, 1
    Int 1