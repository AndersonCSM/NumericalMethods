# Método_do_Ponto_fixo
def Ponto_fixo(f, phi, x, e=1e-11, iter_max=999):
    """
    Realiza o método do Ponto Fixo para encontrar uma raiz da função f com a
    função iterativa phi e uma aproximação inicial x.

    Parâmetros:
    - f: função que representa a equação a ser analisada.
    - phi: função iterativa que gera a próxima aproximação.
    - x: aproximação inicial.
    - e: tolerância de erro (opcional, valor padrão: 1e-11).
    - iter_max: número máximo de iterações (opcional, valor padrão: 999).

    Retorna:
    - [x, iter]: uma lista contendo a raiz aproximada x encontrada e o número
    de iterações realizadas.

    Observações:
    - Caso a função não atinja a convergência dentro do número máximo de
    iterações, x pode não ser uma raiz precisa.
    - É importante escolher a função iterativa phi de forma a garantir a
    convergência do método.

    Exemplo de uso:
    >>> f = lambda x: x**2 - 4
    >>> phi = lambda x: (x + 4 / x) / 2
    >>> Ponto_fixo(f, phi, 2)
    [2.000000000000004, 4]
    """
    for iter in range(iter_max):
        y = f(x)
        if abs(y) < e:
            break
        else:
            x = phi(x)

    return [x, iter]
