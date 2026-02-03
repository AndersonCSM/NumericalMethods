def tabela(listas=[], dicio={}, values=False):
    print(f'{"|":<}{"-=-"*26:^}{"|":>}')
    print(f'{"|":<}{dicio["função"] :^78}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')

    print(f'{"|":<}R**2= {dicio["R_quadrado"]:^12.4f}', end="")
    print(f'{"|":<}tam = {dicio["tamanho"]:^4}', end="")
    print(f'{"|":<}média y = {dicio["media_y"]:^10.4f}', end="")
    print(f'{"|":<}b = {dicio["b"]:^9.4f}', end="")
    print(f'{"|":<}a = {dicio["a"]:^9.4f}{"|":>}')

    print(f'{"|":<}{"-=-"*26:}{"|":>}')
    print(f'{"|":<}{"x":^12}', end="")
    print(f'{"|":<}{"y":^12}', end="")
    print(f'{"|":<}{"xy":^12}', end="")
    print(f'{"|":<}{"x**2":^12}', end="")
    print(f'{"|":<}{"sq_reg":^12}', end="")
    print(f'{"|":<}{"sq_tot":^13}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')

    if values:
        for i in range(dicio["tamanho"]):
            for j in range(0, len(listas)):
                # print(i, j)
                print(f'{"|":<}{listas[j][i]:>12.4f}', end="")
            print(f'{"|":>2}')
        print(f'{"|":<}{"---"*26:}{"|":>}')

    print(f'{"|":<}{dicio["sum_x"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_y"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_xy"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_xquadrado"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_sq_regressão"]:>12.4f}', end="")
    print(f'{"|":<}{dicio["sum_sq_totais"]:>13.4f}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')


def Regressão_Linear(x=[], y=[], show=False, values=False):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    xy = []
    for i in range(n):
        xy.append(x[i] * y[i])
    sum_xy = sum(xy)

    xquadrado = []
    for i in range(n):
        xquadrado.append(x[i] ** 2)
    sum_xquadrado = sum(xquadrado)

    # f = bx + a
    b = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_xquadrado - (sum_x) ** 2)
    a = ((sum_x * sum_xy) - (sum_y * sum_xquadrado)) / (
        (sum_x) ** 2 - (n * sum_xquadrado)
    )

    fy = f"f(x) = {b:.4f}*x + ({a:.4f})"
    media_y = sum_y / n

    sq_regressão = []
    for i in range(n):
        sq_regressão.append(((b * x[i] + a) - media_y) ** 2)
    sum_sq_regressão = sum(sq_regressão)

    sq_totais = []
    for i in range(n):
        sq_totais.append((y[i] - media_y) ** 2)
    sum_sq_totais = sum(sq_totais)

    R_quadrado = sum_sq_regressão / sum_sq_totais

    listas = (x, y, xy, xquadrado, sq_regressão, sq_totais)
    dicio = {
        "tamanho": n,
        "sum_x": sum_x,
        "sum_y": sum_y,
        "sum_xy": sum_xy,
        "sum_xquadrado": sum_xquadrado,
        "media_y": media_y,
        "função": fy,
        "sum_sq_regressão": sum_sq_regressão,
        "sum_sq_totais": sum_sq_totais,
        "R_quadrado": R_quadrado,
        "a": a,
        "b": b,
    }
    if show:
        tabela(listas, dicio, values)

    return f"{a} + {b}*x"


def Regressão_logaritmica(x_old=[], y=[], show=False, values=False):
    from numpy import log as ln

    n = len(x_old)
    x = ln(x_old)

    sum_x = sum(x)
    sum_y = sum(y)

    xy = []
    for i in range(n):
        xy.append(x[i] * y[i])
    sum_xy = sum(xy)

    xquadrado = []
    for i in range(n):
        xquadrado.append(x[i] ** 2)
    sum_xquadrado = sum(xquadrado)

    # f = bx + a
    b = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_xquadrado - (sum_x) ** 2)
    a = ((sum_x * sum_xy) - (sum_y * sum_xquadrado)) / (
        (sum_x) ** 2 - (n * sum_xquadrado)
    )

    fy = f"f(x) = {b:.4f}*ln(x) + ({a:.4f})"
    media_y = sum_y / n

    sq_regressão = []
    for i in range(n):
        sq_regressão.append(((b * x[i] + a) - media_y) ** 2)
    sum_sq_regressão = sum(sq_regressão)

    sq_totais = []
    for i in range(n):
        sq_totais.append((y[i] - media_y) ** 2)
    sum_sq_totais = sum(sq_totais)

    R_quadrado = sum_sq_regressão / sum_sq_totais

    listas = (x, y, xy, xquadrado, sq_regressão, sq_totais)
    dicio = {
        "tamanho": n,
        "sum_x": sum_x,
        "sum_y": sum_y,
        "sum_xy": sum_xy,
        "sum_xquadrado": sum_xquadrado,
        "media_y": media_y,
        "função": fy,
        "sum_sq_regressão": sum_sq_regressão,
        "sum_sq_totais": sum_sq_totais,
        "R_quadrado": R_quadrado,
        "a": a,
        "b": b,
    }
    if show:
        tabela(listas, dicio, values)

    return f"{b}*ln(x) + ({a})"


def Regressão_Exponencial(x=[], y_old=[], show=False, values=False):
    from numpy import log as ln, exp

    n = len(x)
    y = ln(y_old)

    sum_x = sum(x)
    sum_y = sum(y)

    xy = []
    for i in range(n):
        xy.append(x[i] * y[i])
    sum_xy = sum(xy)

    xquadrado = []
    for i in range(n):
        xquadrado.append(x[i] ** 2)
    sum_xquadrado = sum(xquadrado)

    # f = bx + a
    b = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_xquadrado - (sum_x) ** 2)

    a = ((sum_x * sum_xy) - (sum_y * sum_xquadrado)) / (
        (sum_x) ** 2 - (n * sum_xquadrado)
    )

    fy = f"f(x) = {exp(a):.4f}*e^({b:.4f}*x)"

    media_y = sum_y / n

    sq_regressão = []
    for i in range(n):
        sq_regressão.append(((b * x[i] + a) - media_y) ** 2)
    sum_sq_regressão = sum(sq_regressão)

    sq_totais = []
    for i in range(n):
        sq_totais.append((y[i] - media_y) ** 2)
    sum_sq_totais = sum(sq_totais)

    R_quadrado = sum_sq_regressão / sum_sq_totais

    listas = (x, y, xy, xquadrado, sq_regressão, sq_totais)
    dicio = {
        "tamanho": n,
        "sum_x": sum_x,
        "sum_y": sum_y,
        "sum_xy": sum_xy,
        "sum_xquadrado": sum_xquadrado,
        "media_y": media_y,
        "função": fy,
        "sum_sq_regressão": sum_sq_regressão,
        "sum_sq_totais": sum_sq_totais,
        "R_quadrado": R_quadrado,
        "a": exp(a),
        "b": b,
    }
    if show:
        tabela(listas, dicio, values)

    return f"{exp(a)}*exp({b}*x)"


def Regressão_potência(x_old=[], y_old=[], show=False, values=False):
    from numpy import log as ln, exp

    x = ln(x_old)
    y = ln(y_old)

    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    xy = []
    for i in range(n):
        xy.append(x[i] * y[i])
    sum_xy = sum(xy)

    xquadrado = []
    for i in range(n):
        xquadrado.append(x[i] ** 2)
    sum_xquadrado = sum(xquadrado)

    # f = bx + a
    b = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_xquadrado - (sum_x) ** 2)

    a = ((sum_x * sum_xy) - (sum_y * sum_xquadrado)) / (
        (sum_x) ** 2 - (n * sum_xquadrado)
    )

    fy = f"f(x) = {exp(a):.4f}*x^({b:.4f})"
    media_y = sum_y / n

    sq_regressão = []
    for i in range(n):
        sq_regressão.append(((b * x[i] + a) - media_y) ** 2)
    sum_sq_regressão = sum(sq_regressão)

    sq_totais = []
    for i in range(n):
        sq_totais.append((y[i] - media_y) ** 2)
    sum_sq_totais = sum(sq_totais)

    R_quadrado = sum_sq_regressão / sum_sq_totais

    listas = (x, y, xy, xquadrado, sq_regressão, sq_totais)
    dicio = {
        "tamanho": n,
        "sum_x": sum_x,
        "sum_y": sum_y,
        "sum_xy": sum_xy,
        "sum_xquadrado": sum_xquadrado,
        "media_y": media_y,
        "função": fy,
        "sum_sq_regressão": sum_sq_regressão,
        "sum_sq_totais": sum_sq_totais,
        "R_quadrado": R_quadrado,
        "a": exp(a),
        "b": b,
    }
    if show:
        tabela(listas, dicio, values)

    return f"{exp(a)}* x**({b})"
