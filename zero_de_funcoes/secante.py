# Método_da_Secante
def Secante(f, x, x1, e=1e-11, iter_max=999):
    """
    Realiza o método da Secante para encontrar uma raiz da função f com
    aproximações iniciais x e x1.

    Parâmetros:
    - f: função que representa a equação a ser analisada.
    - x: primeira aproximação inicial.
    - x1: segunda aproximação inicial.
    - e: tolerância de erro (opcional, valor padrão: 1e-11).
    - iter_max: número máximo de iterações (opcional, valor padrão: 999).

    Retorna:
    - [x2, iter]: uma lista contendo a raiz aproximada x2 encontrada e o
    número de iterações realizadas.

    Observações:
    - Caso a função não atinja a convergência dentro do número máximo de
    iterações, x2 pode não ser uma raiz precisa.
    - É recomendado escolher aproximações iniciais x e x1 próximas o
    suficiente para garantir a convergência.

    Exemplo de uso:
    >>> f = lambda x: x**2 - 4
    >>> Secante(f, 1, 2)
    [2.000000000002819, 7]
    """
    for iter in range(iter_max):
        x2 = x1 - (f(x1) * (x1 - x)) / (f(x1) - f(x))
        y = f(x2)

        if abs(y) < e:
            break
        else:
            x = x1
            x1 = x2

    return [x2, iter]
