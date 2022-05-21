Fibonacci:
    Mov cx, 0
    Cmp cx, ax
    Jnz FibonacciUno
    Ret
FibonacciUno:
    Mov cx, 1
    Cmp cx, ax
    Jnz FibonacciCalculo
    Ret
FibonacciCalculo:
    Mov bx, ax
    Dec ax
    Dec bx
    Dec bx
    Push bx
    Call Fibonacci
    Mov dx, ax
    Pop bx
    Mov ax, bx
    Push dx
    Call Fibonacci
    Pop dx
    Add ax, dx
    Ret

Entry_point:
    Mov ax, 4
    Call Fibonacci
    Mov bx, 0
    Mov cx, 0
    Int 1