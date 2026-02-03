# Soma_de_Riemann
def Soma_riemann(f, inf, sup, n, extends=False):
    """
    Calcula a aproximação da integral definida da função f usando o método
    da soma de Riemann.

    Parâmetros:
    f (função): A função a ser integrada.
    inf (float): O limite inferior do intervalo de integração.
    sup (float): O limite superior do intervalo de integração.
    n (int): O número de partições para a soma de Riemann.
    extends (bool, opcional): Indica se deve chamar a função Extends para
    calcular e imprimir a solução exata.

    Retorna:
    float: Aproximação da integral usando o método da soma de Riemann.
    """
    x = []
    y = []
    apro = 0
    h = (sup - inf) / n

    for i in range(0, n):
        x.append(inf + i * h)
        y.append(f(x[i]))

        apro += y[i] * h

    if extends:
        from Extends import Extends

        Extends(f, inf, sup, apro)

    return apro
