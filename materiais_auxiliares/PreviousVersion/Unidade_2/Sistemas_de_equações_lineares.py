def printer(A=[]):
    for k in range(len(A)):
        print(A[k])
    print(" ")


def sucessivas(A=[], B=[], disc=False):
    """
    Usado para calcular resolver um sistema com a matriz A sendo
    triangular inferior
    """
    t = len(A)
    x = [0] * t

    for i in range(0, t):
        soma = 0
        for j in range(0, i):
            soma += A[i][j] * x[j]
        x[i] = (B[i] - soma) / A[i][i]

    if disc:
        Discrepante = {}
        for k in range(len(A)):
            print(A[k])
            Discrepante[f"x[{k+1}]"] = x[k]
        print()
        for k, v in Discrepante.items():
            print(f"{k}:{v}")

    return x


def GaussResolver(a=[], b=[], disc=False):
    """
    A função GaussResolver é a implementação do algoritmo de
    retrosubstituição desenvolvido por Gauss
    para achar uma matriz solução(x) a partir de uma
    matriz triangular superior(A) e uma matriz resultado (B).

            A * x = B

    Entrada:
    A: matriz triangular superior: [[], [], ..., []]
    x: matriz solução: [x1, x2, ..., xn]
    B: matriz resultado: [b1, b2, ..., bn]
    disc: O parâmetro disc tem como valor padrão False,
    caso verdadeiro é retornado um print da Matriz triangular
    superior e a matriz solução em forma de dicionário.

    Saida: x = []

    No geral a função GaussResolver é usado como 2ª etapa dos demais métodos
    de soluções de sistemas lineares.
    Observe que a solução x é retornado um dicionário cujo os elementos
    são a matriz solução.
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
            # print(a[k])
            Discrepante[f"x[{k+1}]"] = x[k]
        # print()
        # for k, v in Discrepante.items():
        # print(f'{k}:{v}')

    return x


def Eliminação_Gauss1(a=[], b=[], solution=False):
    """
    O método de Eliminação_Gauss1 consiste em transformar o sistema A * x = b
    em um sistema equivalente
    com matriz dos coeficientes triangular superior, por meio de
    transformações elementares.

        a * x = b -> A * x = B

        A = matriz equivalente de a
        B = matriz equivalente de b
        x = matriz solução.

    O método consiste em duas fases:

    1- Fase de eliminação: é realizado as transformações elementares na
    matriz(a) de maneira a obter uma matriz equivalente(A)
    garantido que as transformações ocorram na matriz resultado(B)

    1.1- Sem pivoteamento: o método Eliminação_Gauss1 não possui
    código para o pivoteamento, logo está sucetível a erros caso o pivô da
    fase de eliminação seja zero.

    2- Fase de substituição: É realizado o chamado da função GaussResolver

    Entrada:
    A: matriz qualquer a ser transformada: [[], [], ..., []]
    x: matriz solução: [x1, x2, ..., xn]
    B: matriz resultado que também será transformada: [b1, b2, ..., bn]
    disc: O parâmetro disc tem como valor padrão False,
    caso verdadeiro é repassado um valor para que ocorra um
    print da matriz superior equivalente e a matriz solução em
    forma de dicionário.

    Saida: matrizes aproximadas: A = [], B = []
    """

    for i in range(len(a)):
        # pivo = abs(a[i][i])
        # indice = i
        # for j in range(i+1, len(a)):
        #    if abs(a[j][i]) > pivo:
        #        pivo = abs(a[j][i])
        #        indice = j

        # FEITO
        # if indice != i:
        #    temp = a[i]
        #    a[i] = a[indice]
        #    a[indice] = temp

        #    tempb = b[i]
        #    b[i] = b[indice]
        #    b[indice] = tempb

        for m in range(i + 1, len(a)):
            multiplicador = a[m][i] / a[i][i]
            for n in range(i, len(a)):
                a[m][n] -= multiplicador * a[i][n]
            b[m] -= multiplicador * b[i]

    if solution:
        GaussResolver(a, b, solution)

    return a, b


def Eliminação_Gauss2(a=[], b=[], solution=False):
    """
    O método de Eliminação_Gauss2 consiste em transformar o sistema A * x = b
    em um sistema equivalente
    com matriz dos coeficientes triangular superior, por meio de
    transformações elementares.

        a * x = b -> A * x = B

        A = matriz equivalente de a
        B = matriz equivalente de b
        x = matriz solução.

    O método consiste em duas fases:

    1- Fase de eliminação: é realizado as transformações elementares na
    matriz(a) de maneira a obter uma matriz equivalente(A)
    garantido que as transformações ocorram na matriz resultado(B)

    1.1- Pivoteamento total: o método Eliminação_Gauss2 realiza processo de
    pivoteamente a todo momento, logo não está sucetível
    a erros caso o pivô da fase de eliminação seja zero, e também, apresenta
    uma matriz equivalente(A) e matriz resultado(B) diferente
    da calculada manualmente.

    2- Fase de substituição: É realizado o chamado da função GaussResolver

    Entrada:
    A: matriz qualquer a ser transformada: [[], [], ..., []]
    x: matriz solução: [x1, x2, ..., xn]
    B: matriz resultado que também será transformada: [b1, b2, ..., bn]
    disc: O parâmetro disc tem como valor padrão False, caso verdadeiro é
    repassado um valor para que ocorra um
    print da matriz superior equivalente e a matriz solução em forma de
    dicionário.

    Saida: matrizes aproximadas: A = [], B = []
    """

    for i in range(len(a)):
        pivo = abs(a[i][i])
        indice = i
        for j in range(i + 1, len(a)):
            if abs(a[j][i]) > pivo:
                pivo = abs(a[j][i])
                indice = j

        if indice != i:
            temp = a[i]
            a[i] = a[indice]
            a[indice] = temp

            tempB = b[i]
            b[i] = b[indice]
            b[indice] = tempB

        for m in range(i + 1, len(a)):
            multiplicador = a[m][i] / a[i][i]
            for n in range(i, len(a)):
                a[m][n] -= multiplicador * a[i][n]
            b[m] -= multiplicador * b[i]

    if solution:
        GaussResolver(a, b, False)

    return a, b


def Eliminação_Gauss3(a=[], b=[], solution=False):
    """
    O método de Eliminação_Gauss3 consiste em transformar o sistema A * x = b
    em um sistema equivalente
    com matriz dos coeficientes triangular superior, por meio de
    transformações elementares.

        a * x = b -> A * x = B

        A = matriz equivalente de a
        B = matriz equivalente de b
        x = matriz solução.

    O método consiste em duas fases:

    1- Fase de eliminação: é realizado as transformações elementares na
    matriz(a) de maneira a obter uma matriz equivalente(A)
    garantido que as transformações ocorram na matriz resultado(B)

    1.1- Pivoteamento parcial: o método Eliminação_Gauss3 realiza processo de
    pivoteamente a todo momento, logo não está sucetível
    a erros caso o pivô da fase de eliminação seja zero, e apresenta uma
    matriz equivalente(A) e matriz resultado(B) similar a
    calculada manualmente.

    2- Fase de substituição: É realizado o chamado da função GaussResolver

    Entrada:
    A: matriz qualquer a ser transformada: [[], [], ..., []]
    x: matriz solução: [x1, x2, ..., xn]
    B: matriz resultado que também será transformada: [b1, b2, ..., bn]
    disc: O parâmetro disc tem como valor padrão False, caso verdadeiro é
    repassado um valor para que ocorra um
    print da matriz superior equivalente e a matriz solução em forma de
    dicionário.

    Saida: matrizes aproximadas: A = [], B = []
    """

    for i in range(len(a)):
        pivo = abs(a[i][i])
        indice = i
        for j in range(i + 1, len(a)):
            if pivo < abs(1e-8):
                pivo = abs(a[j][i])
                indice = j

        if indice != i:
            temp = a[i]
            a[i] = a[indice]
            a[indice] = temp

            tempB = b[i]
            b[i] = b[indice]
            b[indice] = tempB

        for m in range(i + 1, len(a)):
            multiplicador = a[m][i] / a[i][i]
            for n in range(i, len(a)):
                a[m][n] -= multiplicador * a[i][n]
            b[m] -= multiplicador * b[i]

    if solution:
        return GaussResolver(a, b)

    return a, b


def Fatoração_LU(U=[], B=[], solution=False):
    multiplicadores = []
    size = len(U)

    # LINEARIZAR A MATRIZ, OBTENDO A MATRIZ TRIANGULAR SUPERIOR U
    for i in range(size):
        """
        pivo = abs(U[i][i])
        indice = i
        for j in range(i+1, size):
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
        """

        for m in range(i + 1, size):
            multiplicador = U[m][i] / U[i][i]
            multiplicadores.append(multiplicador)
            for n in range(i, size):
                U[m][n] -= multiplicador * U[i][n]
            # b[m] -= multiplicador * b[i] NAO TROCA

    # OBTEM A MATRIZ TRIANGULAR INFERIOR L
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

    return GaussResolver(U, Y, solution)


def Fatoração_LU_Pivo(U=[], B=[], solution=False):
    multiplicadores = []
    # LINEARIZAR A MATRIZ, OBTENDO A MATRIZ TRIANGULAR SUPERIOR U
    size = len(U)
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

    # OBTÉM A MATRIZ TRIANGULAR INFERIOR L
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
        return GaussResolver(U, Y, solution)
    return U, Y


def convergencia(a=[]):
    """
    A função convergencia verifica se dada uma matriz a, ela é diagonalmente
    convergente para que se possa fazer uso
    dos métodos de gauss-Jacobi e gauss-Seidel.

    Parâmetro de entrada:
    a = [] : lista de listas ou  matriz quadrada.

    Saídas: String informando a situação baseado na fundamentação teórica.
    1- 'Diagonalmente dominante por linhas e colunas'
    2- 'Dominante pelas linhas'
    3- 'Dominante pelas colunas'

    Fundamentação Teórica
    A função verifica se a matriz informada é diagonalmente superior,
    validando o critério das linhas e das colunas.
    1. Critério das linhas:
        Os elementos presentes na diagonal da matriz são maiores que a soma
        dos elementos da linhas

        a[i][i] > a[i][1] + a[i][2] + ... a[i][n]

        Sendo verdadeiro somente quando todos os elementos da diagonal
        obedecem esse critério.

    """
    size = len(a)
    sum_x = sum_y = 0
    ok_x = ok_y = 0
    for i in range(size):
        for j in range(size):
            if a[i][i] != a[j][i]:
                sum_x += a[i][j]
                sum_y += a[j][i]

        if a[i][i] > sum_x:
            ok_x += 1

        if a[i][i] > sum_y:
            ok_y += 1

        sum_x = 0
        sum_y = 0

    if ok_x == size and ok_y == size:
        return "Diagonalmente dominante por linhas e colunas"
    elif ok_x == size:
        return "Dominante pelas linhas"
    elif ok_y == size:
        return "Dominante pelas colunas"
    else:
        return "Vai na fé..."


def Gauss_Jacobi(a=[], b=[], solution=False, e=0.05):
    size = len(a)
    x_anterior = [1] * size
    x_atual = [1] * size
    aux_m = [1] * size
    aux = maior = 0

    for l in range(size):
        x_anterior[l] = b[l] / a[l][l]

    while True:
        for i in range(size):
            for j in range(size):
                if i != j:
                    aux += -a[i][j] * x_anterior[j]
                    # O que está acontecendo é a operação: -a * x_{n} de cada
                    # sistema, um de cada vez e sendo armazenado.
                    # print(f'aux_ant -{a[i][j]} * {x_anterior[j]} = {aux}')

            x_atual[i] = 1 / a[i][i] * (b[i] + aux)
            aux = 0

        for l in range(size):
            aux_m[l] = abs(x_atual[l] - x_anterior[l])
            if abs(x_atual[l]) > maior:
                maior = abs(x_atual[l])
        max_distance_rel = max(aux_m) / maior
        maior = 0

        # i = 0
        # print(f'soluçao {i+1}', x_atual)
        # print(f'Distância relativa: ', max_distance_rel)
        # i += 1

        if max_distance_rel < e:
            # print('finish!')
            # print(max_distance_rel)
            return x_atual
        else:
            x_anterior = x_atual[:]  # Não mexer!


def Gauss_Seidel(a=[], b=[], solution=False, e=0.05):
    size = len(a)
    x_anterior = [1] * size
    x_atual = [1] * size
    aux_m = [1] * size
    aux = maior = 0

    for l in range(size):
        x_atual[l] = b[l] / a[l][l]

    while True:
        x_anterior = x_atual[:]
        for i in range(size):
            for j in range(size):
                if i != j:
                    # print(f'aux_ant={aux}')
                    aux += -a[i][j] * x_atual[j]
                    # O que está acontecendo é a operação: -a * x_{n} de cada
                    # sistema, um de cada vez, e sendo armazenado.
                    # print(f'aux_ant -{a[i][j]} * {x_atual[j]} = {aux}')

            x_atual[i] = 1 / a[i][i] * (b[i] + aux)
            aux = 0

        for l in range(size):
            aux_m[l] = abs(x_atual[l] - x_anterior[l])
            if abs(x_atual[l]) > maior:
                maior = abs(x_atual[l])
        max_distance_rel = max(aux_m) / maior
        maior = 0

        if max_distance_rel < e:
            # print('finish!')
            # print(max_distance_rel)
            return x_atual
