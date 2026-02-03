# Convergencia
def convergencia(a=[]):
    """
    Verifica se uma matriz é diagonalmente convergente.

    Parâmetros:
    a (list[list]): Matriz quadrada representada como uma lista de listas.

    Retorna:
    str: Uma das seguintes mensagens:
        - 'Diagonalmente dominante por linhas e colunas'
        - 'Dominante pelas linhas'
        - 'Dominante pelas colunas'
        - 'Não é diagonalmente dominante'

    Fundamentação Teórica:
    A função verifica se a matriz informada é diagonalmente dominante,
    validando o critério das linhas e das colunas.

    Critério das linhas:
    Os elementos da diagonal principal devem ser maiores do que a soma dos
    elementos da mesma linha.

    Critério das colunas:
    Os elementos da diagonal principal devem ser maiores do que a soma dos
    elementos da mesma coluna.

    Um critério não atendido indica que a matriz não é diagonalmente dominante.
    """
    size = len(a)
    is_dominant_by_rows = True
    is_dominant_by_cols = True

    for i in range(size):
        row_sum = 0
        col_sum = 0

        for j in range(size):
            if i != j:
                row_sum += abs(a[i][j])
                col_sum += abs(a[j][i])

        if abs(a[i][i]) <= row_sum:
            is_dominant_by_rows = False

        if abs(a[i][i]) <= col_sum:
            is_dominant_by_cols = False

    if is_dominant_by_rows and is_dominant_by_cols:
        return "Diagonalmente dominante por linhas e colunas"
    elif is_dominant_by_rows:
        return "Dominante pelas linhas"
    elif is_dominant_by_cols:
        return "Dominante pelas colunas"
    else:
        return "Não é diagonalmente dominante"
