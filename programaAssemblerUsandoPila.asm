Sumar:
    Pop bx
    Pop cx
    Pop dx
    Push bx
    Add dx, cx
    Mov ax, dx
    Inc cx
    Ret
Entry_point:
	Mov ax, 0
	Mov cx, 1
Ciclo:
    Push ax
    Push cx
    Call Sumar
	Cmp cx, 10
	Jnz Ciclo