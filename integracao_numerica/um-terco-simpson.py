# Um_Terço_de_Simpsom
def Um_terco(f, inf, sup, n, extends=False):
    """
    Calcula a aproximação da integral definida da função f usando o método de
    um terço de Simpson.

    Parâmetros:
    f (função): A função a ser integrada.
    inf (float): O limite inferior do intervalo de integração.
    sup (float): O limite superior do intervalo de integração.
    n (int): O número de partições para o método de um terço de Simpson.
    extends (bool, opcional): Indica se deve chamar a função Extends para
    calcular e imprimir a solução exata.

    Retorna:
    float: Aproximação da integral usando o método de um terço de Simpson.
    """
    x = []
    y = []

    if n % 2 != 0:
        print("Número de partiçòes inválido!")
        return None

    h = (sup - inf) / n

    for i in range(0, n + 1):
        x.append(inf + i * h)
        y.append(f(x[i]))

    sum_1 = sum_2 = 0
    for i in range(1, len(x) - 1):
        if i % 2 != 0:
            sum_1 += y[i]
        else:
            sum_2 += y[i]

    apro = h / 3 * (y[0] + 4 * sum_1 + 2 * sum_2 + y[-1])

    if extends:
        from Extends import Extends

        Extends(f, inf, sup, apro)

    return apro


def f(x):
    return 1 / x


inf = 1
sup = 3
n = 6
print(Um_terco(f, inf, sup, n))
