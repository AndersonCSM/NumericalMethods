# Regressão_Linear
def Regressão_Linear(x=[], y=[], view="parcial"):
    """
    Realiza a regressão linear simples para um conjunto de dados.

    Parâmetros:
    x (list[float]): Lista contendo os valores de x.
    y (list[float]): Lista contendo os valores de y.
    view (str, opcional): Opção para visualização dos resultados. Pode ser
    "total" para visualização completa ou "parcial" para visualização resumida.

    Retorna:
    None
    """
    n = len(x)

    xy = []
    xquadrado = []

    for i in range(n):
        xy.append(x[i] * y[i])
        xquadrado.append(x[i] ** 2)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xquadrado = sum(xquadrado)
    sum_xy = sum(xy)

    # f = bx + a
    b = ((n * sum_xy) - (sum_x * sum_y)) / (n * sum_xquadrado - (sum_x) ** 2)
    a = ((sum_x * sum_xy) - (sum_y * sum_xquadrado)) / (
        (sum_x) ** 2 - (n * sum_xquadrado)
    )

    media_y = sum_y / n

    sq_regressão = []
    sq_totais = []

    for i in range(n):
        sq_regressão.append(((b * x[i] + a) - media_y) ** 2)
        sq_totais.append((y[i] - media_y) ** 2)

    sum_sq_totais = sum(sq_totais)
    sum_sq_regressão = sum(sq_regressão)

    func = f"f(x) = {b:.4f}*x + ({a:.4f})"
    R_quadrado = sum_sq_regressão / sum_sq_totais

    listas = (x, y, xy, xquadrado, sq_regressão, sq_totais)

    dicio = {
        "tamanho": n,
        "sum_x": sum_x,
        "sum_y": sum_y,
        "sum_xy": sum_xy,
        "sum_xquadrado": sum_xquadrado,
        "media_y": media_y,
        "função": func,
        "sum_sq_regressão": sum_sq_regressão,
        "sum_sq_totais": sum_sq_totais,
        "R_quadrado": R_quadrado,
        "a": a,
        "b": b,
    }

    if view.strip().lower() == "total":
        from Extends import tabela

        tabela(listas, dicio)

    elif view.strip().lower() == "parcial":
        print("-=-" * 15)
        print(func)
        print("-=-" * 15)
        print(f" R^2: {dicio['R_quadrado']:>9.4f}")
        print(" f = bx + a")
        print(f' b = {dicio["b"]:>9.4f}')
        print(f' a = {dicio["a"]:>9.4f}')
        print("-=-" * 15)
