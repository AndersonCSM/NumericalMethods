# Três_Oitavos_de_Simpsom
def Tres_oitavos(f, inf, sup, n, extends=False):
    """
    Calcula a aproximação da integral definida da função f usando o método de
    três oitavos de Simpson.

    Parâmetros:
    f (função): A função a ser integrada.
    inf (float): O limite inferior do intervalo de integração.
    sup (float): O limite superior do intervalo de integração.
    n (int): O número de partições para o método de três oitavos de Simpson.
    extends (bool, opcional): Indica se deve chamar a função Extends para
    calcular e imprimir a solução exata.

    Retorna:
    float: Aproximação da integral usando o método de três oitavos de Simpson.
    """
    x = []
    y = []

    if n % 3 != 0:
        print("Número de partições não é múltiplo de 3!")

        return None

    h = (sup - inf) / n

    for i in range(0, n + 1):
        x.append(inf + i * h)
        y.append(f(x[i]))

    sum_y1 = sum_y2 = 0
    for i in range(1, len(x) - 1):
        if i % 3 != 0:
            sum_y1 += y[i]
        else:
            sum_y2 += y[i]

    apro = h * 3 / 8 * (y[0] + 3 * sum_y1 + 2 * sum_y2 + y[-1])

    if extends:
        from Extends import Extends

        Extends(f, inf, sup, apro)

    return apro


def f(x):
    return 1 / x


inf = 1
sup = 3
n = 6
print(Tres_oitavos(f, inf, sup, n))
