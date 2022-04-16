Sumar:
    Pop bx
    Pop cx
    Pop dx
    Push bx
    Add dx, cx
    Mov ax, dx
    Inc cx
    Ret