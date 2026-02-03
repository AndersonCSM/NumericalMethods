# Isolamento_de_raizes


def Isolamento_de_raizes(f, lim_f, lim_s, h):
    """
    Realiza o isolamento das raízes de uma função no intervalo [lim_f, lim_s]
    com um passo de tamanho h.

    Parâmetros:
    - f: função que representa a equação a ser analisada.
    - lim_f: limite inferior do intervalo de análise.
    - lim_s: limite superior do intervalo de análise.
    - h: tamanho do passo entre os valores avaliados.

    Retorna:
    - raiz: uma lista contendo tuplas representando os intervalos onde as
    raízes estão isoladas.

    Exemplo de uso:
    >>> f = lambda x: x**2 - 4
    >>> Isolamento_de_raizes(f, -5, 5, 0.5)
    [(1.5, 2.0), (-2.0, -1.5)]
    """
    raiz = []
    i = lim_f + h
    while i <= lim_s:
        if f(i - h) * f(i) < 0:
            raiz.append((i - h, i))
        i += h
    return raiz
