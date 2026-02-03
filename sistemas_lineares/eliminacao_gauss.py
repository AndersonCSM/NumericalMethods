# Eliminação_de_Gauss
def Eliminacao_gauss(a=[], b=[], pivoteamento="total"):
    """
    pivoteamentos = ['total', 'parcial', 'nenhum']

    O método de Eliminação de Gauss consiste em transformar o sistema
    A * x = b em um sistema equivalente
    com matriz dos coeficientes triangular superior, por meio de
    transformações elementares.

    a * x = b -> A * x = B

    A = matriz equivalente de a
    B = matriz equivalente de b
    x = matriz solução.

    O método consiste em duas fases:

    1- Fase de eliminação: são realizadas as transformações elementares na
    matriz (a) de maneira a obter uma matriz equivalente (A),
    garantindo que as transformações ocorram também na matriz resultado (B).

    1.1- Pivoteamento total: o método de Eliminação de Gauss realiza o
    pivoteamento em todos os momentos, garantindo que não ocorram erros
    caso o pivô da fase de eliminação seja zero.
    Além disso, apresenta uma matriz equivalente (A) e uma matriz resultado (B)
    diferentes das calculadas manualmente.

    1.2- Pivoteamento parcial: o método de Eliminação de Gauss realiza o
    pivoteamento parcial em todos os momentos, garantindo que não ocorram
    erros caso o pivô da fase de eliminação seja zero.
    Apresenta uma matriz equivalente (A) e uma matriz resultado (B)
    semelhantes às calculadas manualmente.

    1.3- Sem pivoteamento: o método de Eliminação de Gauss não realiza
    pivoteamento, sendo suscetível a erros caso o pivô da fase de eliminação
    seja zero.

    2- Fase de substituição: é realizado o chamado da função Retrosubstituição
    para obter a solução do sistema.

    Entrada:
    a: matriz qualquer a ser transformada: [[], [], ..., []]
    b: matriz resultado que também será transformada: [b1, b2, ..., bn]
    pivoteamento: parâmetro opcional que define o tipo de pivoteamento a ser
    utilizado ('total' por padrão), podendo assumir os valores: 'total',
    'parcial', 'nenhum'.

    Saída: matrizes aproximadas: a = [], b = []
    """
    if pivoteamento.lower().strip() == "total":
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

    elif pivoteamento.lower().strip() == "parcial":
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

    elif pivoteamento.lower().strip() == "nenhum":
        for i in range(len(a)):
            for m in range(i + 1, len(a)):
                multiplicador = a[m][i] / a[i][i]
                for n in range(i, len(a)):
                    a[m][n] -= multiplicador * a[i][n]
                b[m] -= multiplicador * b[i]

    return a, b
