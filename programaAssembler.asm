	Mov Ax, 0
Entry_point:
	Mov cx, 1
Ciclo:
	Add ax, cx
	Inc cx
	Cmp cx, 10
	Jnz Ciclo