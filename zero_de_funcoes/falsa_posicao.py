# Método_da_Falsa_Posição
def Falsa_Posição(f, a, b, e=1e-11, iter_max=999):
    """
    Realiza o método da Falsa Posição para encontrar uma raiz da função f
    no intervalo [a, b].

    Parâmetros:
    - f: função que representa a equação a ser analisada.
    - a: limite inferior do intervalo de análise.
    - b: limite superior do intervalo de análise.
    - e: tolerância de erro (opcional, valor padrão: 1e-11).
    - iter_max: número máximo de iterações (opcional, valor padrão: 999).

    Retorna:
    - [x, iter]: uma lista contendo a raiz aproximada x encontrada e o número
    de iterações realizadas.

    Observações:
    - Caso a função não atinja a convergência dentro do número máximo de
    iterações, x pode não ser uma raiz precisa.
    - É recomendado que a função f seja contínua no intervalo [a, b] e que
    f(a) * f(b) < 0, indicando a presença de pelo menos uma raiz no intervalo.

    Exemplo de uso:
    >>> f = lambda x: x**2 - 4
    >>> Falsa_Posição(f, 1, 3)
    [2.00000000001, 3]
    """
    for iter in range(iter_max):
        x = (f(b) * a - f(a) * b) / (f(b) - f(a))
        y = f(x)

        if abs(y) < e:
            break
        else:
            if f(a) * y < 0:
                b = x
            else:
                a = x

    return [x, iter]
