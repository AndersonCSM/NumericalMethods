def showler(inf=0, sup=0, s=0, fun=''):
    from sympy import integrate, symbols
    
    x = symbols('x')
    s_exct = integrate(fun, (x, inf, sup)).evalf()
    print('--'*15)
    print(f'Solução aproximada: {s:>10.4f}')
    print(f'Solução exata: {s_exct:>15.4f}')
    print(f'Erro absoluto: {abs(s_exct - s):>15.4f}')
    print(f'Erro relativo: {(abs(s_exct - s)/s_exct)*100:>13.4f} %')
    print('--'*15)

def Trapézio(inf=0, sup=0, partições=1, fun='', show= False):
    from numpy import arange
    
    h = (sup - inf)/partições
    fun_up = fun.replace('x','x[i]')

    x, y = [], []
    for i in arange(inf, sup, h):
        x.append(i)
    x.append(sup)

    size = len(x)
    for i in range(size):
        y.append(float(eval(fun_up)))

    sum_y = 0
    for i in range(1,size-1):
        sum_y += y[i]

    s =  h/2 * ( y[0] + 2*sum_y + y[-1])

    if show:
        showler(inf, sup,  s, fun)
    else:
        return s


def Simpson_um_Terço(inf=0, sup=0, partições=1, fun='', show= False):
    from numpy import arange

    if partições % 2 != 0:
        return f'Número de partições não é par! {partições}'
    
    h = (sup - inf)/partições
    fun_up = fun.replace('x','x[i]')

    x, y = [], []
    xi = []
    for i in range(1, partições):
        xi = a + i*h
        
    for i in arange(inf, sup, h):
        x.append(i)
    x.append(sup)

    size = len(x)
    for i in range(size):
        y.append(float(eval(fun_up)))

    sum_y1 = sum_y2 = 0
    for i in range(1,size-1):
        if i % 2 != 0:
            sum_y1 += y[i]
        else:
            sum_y2 += y[i]

    s =  h/3 * ( y[0] + 4*sum_y1 + 2 * sum_y2 + y[-1])

    if show:
        showler(inf, sup,  s, fun)
    else:
        return s


def Simpson_Três_Oitavos(inf=0, sup=0, partições=1, fun='', show= False):
    from numpy import arange
    if partições % 3 != 0:
        return f'Número de partições não é múltiplo de 3! {partições}'
    
    h = (sup - inf)/partições
    fun_up = fun.replace('x','x[i]')

    x, y = [], []
    for i in arange(inf, sup, h):
        x.append(i)
    x.append(sup)

    size = len(x)
    for i in range(size):
        y.append(float(eval(fun_up)))

    sum_y1 = sum_y2 = 0
    for i in range(1,size-1):
        if i % 3 != 0:
            sum_y1 += y[i]
        else:
            sum_y2 += y[i]

    s =  h* 3/8 * ( y[0] + 3*sum_y1 + 2 * sum_y2 + y[-1])

    if show:
        showler(inf, sup,  s, fun)
    else:
        return s