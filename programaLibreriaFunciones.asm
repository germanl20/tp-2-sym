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
    Mov cx, 0
    Mov dx, 0
    Cmp cx, bx
    Jnz CicloMultiplicar
    Mov ax, 0
    Ret
CicloMultiplicar:
    Inc cx
    Add dx, ax
    Cmp cx, bx
    Jnz CicloMultiplicar
    Mov ax, dx
    Ret

Dividir:
    Pop cx
    Pop ax
    Pop bx
    Push cx
    Mov cx, 0
    Mov dx, 0
CicloDividir:
    Inc cx
    Add dx, bx
    Cmp dx, ax
    Jnz CicloDividir
    Cmp ax, dx
    Jnz CalcularResultados
    Mov ax, cx
    Mov bx, 0
    Ret
CalcularResultados:
    Dec cx
    Push ax
    Push bx
    Push cx
    Push bx
    Push cx
    Call Multiplicar
    Mov dx, ax
    Pop cx
    Pop bx
    Pop ax
    Push cx
    Push dx
    Push ax
    Call Restar
    Mov bx, ax
    Pop ax
    Ret

RaizCuadrada:
    Pop cx
    Pop ax
    Push cx
    Mov bx, 0
CicloRaizCuadrada:
    Inc bx
    Push ax
    Push bx
    Push bx
    Push bx
    Call Multiplicar
    Mov dx, ax
    Pop bx
    Pop ax
    Cmp dx, ax
    Jnz CicloRaizCuadrada
    Cmp ax, dx
    Jnz CalcularResultadosRaizCuadrada
    Mov ax, bx
    Ret
CalcularResultadosRaizCuadrada:
    Dec bx
    Mov ax, bx
    Ret