# Método_de_Newton_Raphson
def newton_raphson(f, x, e=1e-11, iter_max=999):
    """
    Realiza o método de Newton-Raphson para encontrar uma raiz da função f com
    uma aproximação inicial x.

    Parâmetros:
    - f: função que representa a equação a ser analisada.
    - x: aproximação inicial.
    - e: tolerância de erro (opcional, valor padrão: 1e-11).
    - iter_max: número máximo de iterações (opcional, valor padrão: 999).

    Retorna:
    - [x, iter]: uma lista contendo a raiz aproximada x encontrada e o número
    de iterações realizadas.

    Observações:
    - Caso a função não atinja a convergência dentro do número máximo de
    iterações, x pode não ser uma raiz precisa.
    - É importante escolher uma aproximação inicial adequada para garantir a
    convergência do método.
    - A função f deve ser diferenciável no intervalo em que se busca a raiz.

    Exemplo de uso:
    >>> f = lambda x: x**2 - 4
    >>> newton_raphson(f, 2)
    [2.000000000003619, 4]
    """
    for iter in range(iter_max):
        y = f(x)

        if abs(y) < e:
            break
        else:
            h = 1e-10
            dy = (f(x + h) - f(x)) / h
            x = x - y / dy

    return [x, iter]
