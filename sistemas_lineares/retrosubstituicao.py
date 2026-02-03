# Retrosubstituição
def Retrosubstituicao(a=[], b=[], disc=False):
    """
    Resolve um sistema linear utilizando o método de Retrosubstituição.

    A função Retrosubstituicao realiza a retrosubstituição em uma matriz
    triangular superior (A)
    e um vetor resultado (b) para obter a matriz solução (x).

    Entradas:
    A: Matriz triangular superior representada como uma lista de listas [[]].
    b: Vetor resultado representado como uma lista [].
    disc: Parâmetro opcional que controla a exibição da matriz triangular
    superior e da matriz solução em forma de dicionário (False por padrão).

    Saída:
    x: Matriz solução representada como uma lista [].

    Observações:
    - A função Retrosubstituicao é geralmente usada como a segunda etapa de
    outros métodos de solução de sistemas lineares.
    - A solução x é retornada como uma lista.
    - Se o parâmetro disc for True, a função exibirá a matriz triangular
    superior e a matriz solução em forma de dicionário.

    Exemplo de uso:
    >>> A = [[3, 2, 1], [0, 2, 1], [0, 0, 1]]
    >>> b = [1, 2, 3]
    >>> Retrosubstituicao(A, b, disc=True)
    [1.0, 0.0, 3.0]
    """

    t = len(a)
    x = [0] * t

    for i in range(t - 1, -1, -1):
        soma = 0
        for j in range(i + 1, t):
            soma += a[i][j] * x[j]
        x[i] = (b[i] - soma) / a[i][i]

    if disc:
        Discrepante = {}
        for k in range(len(a)):
            Discrepante[f"x[{k+1}]"] = x[k]
        return Discrepante

    return x
