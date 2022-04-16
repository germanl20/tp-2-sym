Entry_point:
	Mov Ax, 0
	Mov cx, 1
Ciclo:
	Include "programaAssemblerInclude.asm"
	Cmp cx, 10
	Jnz Ciclo