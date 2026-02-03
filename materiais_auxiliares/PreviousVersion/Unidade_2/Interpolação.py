def Interpolação_Linear(x=[], y=[], p=0, polinomio=False):
    try:
        """
        A interpolação linear como visto na disciplina se resume a achar os
        termos a[0] e a[1] e resolver o polinômio de grau 1.
        f(x) = a[0] + a[1]*x

        A função recebe de entrada:
        x = [] : lista dos valores de x
        y = [] : lista dos valores de y
        p = float : ponto repassado ao polinômio f(p)

        Caso queira cálcular um ponto em x, dado y, basta inverter a
        entrada das lista, ou seja, x recebe a lista de e y a de x.

        Saída: valor numérico(float) do ponto aproximado do polinômio.
        """

        a0 = ((y[0] * x[1]) - (y[1] * x[0])) / (x[1] - x[0])
        a1 = (y[1] - y[0]) / (x[1] - x[0])
        if polinomio:
            return f"f(x) = {a0} + {a1} * x"
        return a0 + a1 * p
    except:
        return "Não foi possível estimar"


def Método_Lagrange(x=[], y=[], x_v=0, polinomio=False):
    try:
        size = len(x)
        llist = [1] * size
        p_x = 0

        # l[0] = ((x_v - x[1])/(x[0] - x[1])) * ((x_v - x[2])/(x[0] - x[2])) *
        # ((x_v - x[3])/(x[0] - x[3]))

        # for i in range(size):
        # l[i] = ((x_v - x[1])/(x[i] - x[1])) * ((x_v - x[2])/(x[i] - x[2])) *
        # ((x_v - x[3])/(x[i] - x[3]))

        for i in range(size):
            for j in range(size):
                if i != j:
                    llist[i] *= (x_v - x[j]) / (x[i] - x[j])

        for i in range(size):
            # p_x = y[0]*l[0][x] + y[1]*l[1][x] + y[2]*l[2][x]
            p_x += y[i] * llist[i]
        return p_x
    except:
        return "Não foi possível estimar"


def Método_Newton(x=[], y=[], x_v=0, polinomio=False):
    try:
        size = len(x)

        """
        d{0}[] = y[:]
        d{1}[0] = ((y[1]-y[0])/(x[1]-x[0]))
        d{1}[1] = ((y[2]-y[1])/(x[2]-x[1]))
        d{2}[0] = ((d{1}[1]-d{1}[0])/(x[2]-x[0]))
        d{n}[0] = ((d{n}[1]-d{n-1}[0])/(x[n]-x[0]))

        d = {d0:[], d1:[], d2:[], dn:[]}
        d = [[], [], [], []]
        """

        aux = []
        d = []
        for i in range(size):
            for j in range(size - i, 0, -1):
                aux.append(1)
            d.append(aux[:])
            aux.clear()

        for i in range(size):
            if i == 0:
                d[i] = y[:]
            else:
                aux = size - i
                for j in range(aux):
                    d[i][j] = (d[i - 1][j + 1] - d[i - 1][j]) / (x[i + j] - x[j])

            """
            d[0]    = y[:] ok

            aux = 3 - 1 = 2, i = 1
            d[1][0] = ((d[0][1] -      d[0][0])  / (x[1]-x[0]))
            d[1][1] = ((d[0][2] -      d[0][1])  / (x[2]-x[1]))
            d[i][j] = ((d[i-1][j+1]-   d[i-1][j]) / (x[i+j]-x[j]))

            aux = 3 - 2 = 1, i = 2
            d[2][0] = ((d[1][1] -       d[1][0]) / (x[2]-x[0]))
            d[i][j] = ((d[i-1][j+1] -   d[i-1][j]) / (x[i+j]-x[j]))

            # p_x = d[0][0] + d[i][0] * (x_v - x[0]) + d[2][0] *
            #  (x_v - x[0]) * (x_v - x[1]):

            d[1][0] (x - x[0])
            d[2][0] (x - x[0]) (x - x[1])
            d[3][0] (x - x[0]) (x - x[1]) (x - x[2])
            d[n][0] (x - x[0]) (x - x[1]) (x - x[n-1])

            m[0] = (x - x[0])
            m[1] = m[0] * (x - x[1])
            m[2] = m[1] * (x - x[2])
            m[n] = m[n-1] * (x - x[n])

            m = 1
            p_x = 0
            for n in range(size):
                m *= (x - x[n])
                if n != 0:
                    p_x += d[n][0] * m

            p_x = d[0][0] + p_x
            """

        m = 1
        p_x = 0
        for n in range(size):
            p_x += d[n][0] * m
            m *= x_v - x[n]

        # print(d)
        return p_x
    except:
        return "Não foi possível estimar"
