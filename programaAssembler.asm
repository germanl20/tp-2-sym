Include "programaAssemblerInclude.asm"

Entry_point:
	Mov ax, 0
	Mov cx, 1

Ciclo:
    Push ax
    Push cx
    Call Sumar
	Cmp cx, 10
	Jnz Ciclo