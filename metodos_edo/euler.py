def euler_method(ed, y0, t0, n, h):
    """
    Implementação do método de Euler para resolver EDOs de primeira ordem.

    Parâmetros:
    - ed: Função que define a EDO (dy/dx = f(x, y))
    - y0: Condição inicial para y
    - t0: Condição inicial para t
    - n: Quantidades de partições
    - h: Tamanho do passo

    Retorna:
    - x: Lista dos valores de t calculados
    - y: Lista dos valores de y calculados
    """

    t = [t0]  # adiciona o ponto inicial a lista
    y = [y0]  # adiciona o ponto inicial a lista

    for i in range(1, n+1):  # percorre a lista
        t_m = t0 + i * h
        y_m = y[i-1] + h * ed(y[i - 1], t[i - 1])

        y.append(y_m)  # adiciona os valores a lista
        t.append(t_m)  # adiciona os valores a lista

    return t, y
