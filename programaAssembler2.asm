Entry_point:
	Mov Ax, 0
	Mov cx, 1
Ciclo:
	Add ax, cx
	Inc cx
	Cmp cx, 10
	Jnz Ciclo