# Método_de_Lagrange
def Método_Lagrange(x=[], y=[], x_v=0):
    """
    Implementação do Método de Lagrange para interpolação polinomial.

    O Método de Lagrange é um método de interpolação que utiliza polinômios
    de Lagrange para estimar o valor de uma função em um ponto desconhecido
    com base em um conjunto de pontos conhecidos.

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
        llist = [1] * size
        p_x = 0

        for i in range(size):
            for j in range(size):
                if i != j:
                    llist[i] *= (x_v - x[j]) / (x[i] - x[j])

        for i in range(size):
            p_x += y[i] * llist[i]
        return p_x
    except (ValueError, ZeroDivisionError, IndexError) as e:
        return f"Não foi possível estimar: {str(e)}"
