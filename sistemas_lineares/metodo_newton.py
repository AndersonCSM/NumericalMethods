# Método_de_Newton
def Método_Newton(x=[], y=[], x_v=0):
    """
    Implementação do método de Newton para interpolação polinomial.

    O método de Newton é um método para encontrar o polinômio interpolador de
    Newton para um conjunto de pontos dados. Ele é baseado na ideia de
    diferenças divididas e fornece uma maneira eficiente de calcular o valor
    interpolado em um novo ponto.

    Parâmetros:
    x (list): Lista dos valores x dos pontos conhecidos.
    y (list): Lista dos valores y dos pontos conhecidos.
    x_v (float): Ponto em que se deseja calcular o valor interpolado.

    Retorna:
    float or str: Valor interpolado em x_v.
    Em caso de erro, retorna uma mensagem indicando a impossibilidade
    de estimar.
    """
    try:
        size = len(x)
        aux = []
        d = []
        for i in range(size):
            for j in range(size - i, 0, -1):
                aux.append(1)
            d.append(aux[:])
            aux.clear()

        for i in range(size):
            if i == 0:
                d[i] = y[:]
            else:
                aux = size - i
                for j in range(aux):
                    d[i][j] = (d[i - 1][j + 1] - d[i - 1][j]) / (x[i + j] - x[j])

        m = 1
        p_x = 0
        for n in range(size):
            p_x += d[n][0] * m
            m *= x_v - x[n]

        return p_x

    except (ValueError, ZeroDivisionError, IndexError) as e:
        return f"Não foi possível estimar: {str(e)}"
