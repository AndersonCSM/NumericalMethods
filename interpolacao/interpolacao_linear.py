# Interpolação_Linear
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

        Caso queira calcular um ponto em x, dado y, basta inverter a
        entrada das listas, ou seja, x recebe a lista de e y a de x.

        Saída: valor numérico (float) do ponto aproximado do polinômio.
        """

        if len(x) != 2 or len(y) != 2:
            raise ValueError("As listas de x e y devem ter 2 elementos")

        if x[1] == x[0]:
            raise ValueError("Os valores de x devem ser diferentes")

        a0 = ((y[0] * x[1]) - (y[1] * x[0])) / (x[1] - x[0])
        a1 = (y[1] - y[0]) / (x[1] - x[0])

        if polinomio:
            return f"f(x) = {a0} + {a1} * x"

        return a0 + a1 * p

    except (ValueError, ZeroDivisionError, IndexError) as e:
        return f"Não foi possível estimar: {str(e)}"
