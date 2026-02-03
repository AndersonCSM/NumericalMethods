# Trapézio
def Trapezio(f, inf, sup, n, extends=False):
    """
    Calcula a aproximação da integral definida da função f usando o método
    do trapézio.

    Parâmetros:
    f (função): A função a ser integrada.
    inf (float): O limite inferior do intervalo de integração.
    sup (float): O limite superior do intervalo de integração.
    n (int): O número de partições para o método do trapézio.
    extends (bool, opcional): Indica se deve chamar a função Extends para
    calcular e imprimir a solução exata.

    Retorna:
    float: Aproximação da integral usando o método do trapézio.
    """
    x = []
    y = []

    h = (sup - inf) / n

    for i in range(0, n + 1):
        x.append(inf + i * h)
        y.append(f(x[i]))

    sum_y = 0
    for i in range(1, len(x) - 1):
        sum_y += y[i]

    apro = h / 2 * (y[0] + 2 * sum_y + y[-1])

    if extends:
        from Extends import Extends

        Extends(f, inf, sup, apro)

    return apro


def f(x):
    return 1 / x


inf = 1
sup = 3
n = 4
print(Trapezio(f, inf, sup, n))
