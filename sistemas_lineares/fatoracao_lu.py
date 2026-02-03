# Fatoração_LU
def Fatoracao_LU(U=[], B=[], solution=False, pivoteamento="total"):
    """
    Realiza a fatoração LU de uma matriz U e resolve o sistema linear
    U * x = B.

    Entrada:
    U: matriz U a ser fatorada
    B: matriz B do sistema linear
    solution: indica se deve ser retornada a solução do sistema linear
    pivoteamento: tipo de pivoteamento a ser utilizado ('total' ou 'nenhum')

    Saída:
    Matriz U fatorada e, se solution for True, a solução do sistema linear
    U * x = B
    """
    if pivoteamento.lower().strip() == "total":
        multiplicadores = []
        size = len(U)

        # Lineariza a matriz, obtendo a matriz triangular superior U
        for i in range(size):
            pivo = abs(U[i][i])
            indice = i

            for j in range(i + 1, size):
                if abs(U[j][i]) > pivo:
                    pivo = abs(U[j][i])
                    indice = j

            if indice != i:
                temp = U[i]
                U[i] = U[indice]
                U[indice] = temp

                tempB = B[i]
                B[i] = B[indice]
                B[indice] = tempB

            for m in range(i + 1, size):
                multiplicador = U[m][i] / U[i][i]
                multiplicadores.append(multiplicador)
                for n in range(i, size):
                    U[m][n] -= multiplicador * U[i][n]
                # b[m] -= multiplicador * b[i] NAO PRECISA FAZER

        # Obtém a matriz triangular inferior L
        Laux, L = [], []
        k = 0
        for i in range(size):
            for j in range(size):
                if i == j:
                    Laux.append(1)
                elif i > j:
                    Laux.append(multiplicadores[k])
                    k += 1
                else:
                    Laux.append(0)
            L.append(Laux[:])
            Laux.clear()

        # Obtendo Y através das substituições sucessivas
        # L * Y = B
        t = len(L)
        Y = [0] * t

        for i in range(0, t):
            soma = 0
            for j in range(0, i):
                soma += L[i][j] * Y[j]
            Y[i] = (B[i] - soma) / L[i][i]

        if solution:
            from Retrosubstituicao import Retrosubstituicao

            return Retrosubstituicao(U, Y)

        return U, Y

    elif pivoteamento.lower().strip() == "nenhum":
        multiplicadores = []
        size = len(U)

        # Lineariza a matriz, obtendo a matriz triangular superior U
        for i in range(size):
            for m in range(i + 1, size):
                multiplicador = U[m][i] / U[i][i]
                multiplicadores.append(multiplicador)
                for n in range(i, size):
                    U[m][n] -= multiplicador * U[i][n]
                # b[m] -= multiplicador * b[i] NAO TROCA

        # Obtém a matriz triangular inferior L
        Laux, L = [], []
        k = 0
        for i in range(size):
            for j in range(size):
                if i == j:
                    Laux.append(1)
                elif i > j:
                    Laux.append(multiplicadores[k])
                    k += 1
                else:
                    Laux.append(0)
            L.append(Laux[:])
            Laux.clear()

        # Obtendo Y através de substituições sucessivas
        # L * Y = B
        t = len(L)
        Y = [0] * t

        for i in range(0, t):
            soma = 0
            for j in range(0, i):
                soma += L[i][j] * Y[j]
            Y[i] = (B[i] - soma) / L[i][i]

        if solution:
            from Retrosubstituicao import Retrosubstituicao

            return Retrosubstituicao(U, Y)

        return U, Y
