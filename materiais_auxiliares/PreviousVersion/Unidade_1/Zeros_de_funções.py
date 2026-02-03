def limpeza():
    a_list = []
    b_list = []
    x_list = []
    fx_list = []
    fa_list = []
    fb_list = []

    a_list.clear()
    b_list.clear()
    x_list.clear()
    fx_list.clear()
    fa_list.clear()
    fb_list.clear()


def Bissecao(eq="", a=0, b=0, e=0.01, strike=False, iteration=100):
    try:
        limpeza()
        i = 0
        """
        A função Bissecao utiliza do método de mesmo nome para achar uma raiz
        aproximada. Ela apresenta os parâmetros:

        eq : string -> função matemática a ser calculada, escrita em uma
        string;
        a : int/float -> menor valor do intervalo;
        b : int/float -> maior valor do intervalo;
        e : int/float -> precisão numérica da raiz aproximada;
        show : Bool -> Em breve.
        """
        a_list = []
        b_list = []
        x_list = []
        fx_list = []

        while i < iteration:
            x = (a + b) / 2
            fx = float(eval(eq))

            if strike:
                a_list.append(a)
                b_list.append(b)
                x_list.append(x)
                fx_list.append(fx)

            if abs(fx) < e:
                break
            else:
                fa = float(eval(eq.replace("x", "a")))
                if fa * fx < 0:
                    b = x
                else:
                    a = x
            i += 1

        if strike:
            if i == iteration or not (a <= x <= b):
                return {}

            return {"a": a_list, "b": b_list, "x": x_list, "f(x)": fx_list}

        if i == iteration or not (a <= x <= b):
            return "Não existe raiz no intervalo com a configuração definida"

        return x
    except:
        if strike:
            return {}

        return "Erro, não foi possível achar a raiz"


def Falsa_posicao(eq="", a=0, b=0, e=0.01, strike=False, iteration=100):
    try:
        limpeza()
        i = 0
        """
        A função Falsa_posicao é a implementação do método numérico de mesmo
        nome que retorna o valor de uma raiz aproximada. Ela apresenta os
        parâmetros:

        eq : string -> função matemática a ser calculada escrita em uma string;
        a : int/float -> menor valor do intervalo;
        b : int/float -> maior valor do intervalo;
        e : int/float -> precisão numérica da raiz aproximada;
        show : Bool -> Em breve.
        """
        a_list = []
        b_list = []
        fa_list = []
        fb_list = []
        x_list = []
        fx_list = []

        while i < iteration:
            fa = float(eval(eq.replace("x", "a")))
            fb = float(eval(eq.replace("x", "b")))
            x = float((a * fb - b * fa) / (fb - fa))
            fx = float(eval(eq))

            if strike:
                a_list.append(a)
                b_list.append(b)
                fa_list.append(fa)
                fb_list.append(fb)
                x_list.append(x)
                fx_list.append(fx)

            if abs(fx) < e:
                break
            else:
                if fa * fx < 0:
                    b = x
                else:
                    a = x
            i += 1

        if strike:
            if i == iteration or not (a <= x <= b):
                return {}
            else:
                return {
                    "a": a_list,
                    "f(a)": fa_list,
                    "b": b_list,
                    "f(b)": fb_list,
                    "x": x_list,
                    "f(x)": fx_list,
                }

        if i == iteration or not (a <= x <= b):
            return "Não existe raiz no intervalo com a configuração definida"
        else:
            return x
    except:
        if strike:
            return {}
        return "Erro, não foi possível achar a raiz"


def Ponto_fixo(eq="", phi="", x=0, e=0.01, strike=False, iteration=100):
    try:
        limpeza()
        i = 0
        """
        A função Ponto_fixo é a implementação do método numérico de mesmo nome
        que retorna o valor de uma raiz aproximada. Ela apresenta parâmetros:

        eq : string -> função matemática a ser calculada escrita em uma string;
        phi: string -> uma função obtida a partir da função base, seguindo os
        critérios do método;
        x : int/float -> chute inicial de uma raiz;
        e : int/float -> precisão numérica da raiz aproximada;
        show : Bool -> Em breve.
        """
        x_list = []
        fx_list = []

        while i < iteration:
            fx = float(eval(eq))

            if strike:
                x_list.append(x)
                fx_list.append(fx)

            if abs(fx) < e:
                break
            else:
                x = float(eval(phi))
            i += 1

        if strike:
            if i == iteration:
                return {}
            else:
                return {"x": x_list, "f(x)": fx_list}

        if i == iteration:
            return "Não existe raiz no intervalo com a configuração definida"
        else:
            return x

    except:
        if strike:
            return {}
        return "Erro, não foi possível achar a raiz"


def Newton_raphson(eq="", x=0, e=0.01, strike=False, iteration=100):
    try:
        limpeza()
        i = 0
        """
        OBSERVAÇÃO: para que a função funcione corretamente é preciso ter a
        biblioteca sympy instalada.

        A função Newton_raphson é a implementação do método numérico,
        retornando o valor de uma raiz aproximada. Ela apresenta os parâmetros:

        eq : string -> função matemática a ser calculada escrita em uma string;
        x : int/float -> chute inicial de uma raiz;
        e : int/float -> precisão numérica da raiz aproximada;
        show : Bool -> Em breve.
        """
        x_list = []
        fx_list = []

        from sympy import diff, symbols

        while i < iteration:
            fx = float(eval(eq))
            simbolo = symbols("x")
            dxexpress = str(diff(eq, simbolo))
            dx = float(eval(dxexpress))

            if strike:
                x_list.append(x)
                fx_list.append(fx)

            if abs(fx) < e:
                break
            else:
                x = float(x - (fx / dx))
            i += 1

        if strike:
            if i == iteration:
                return {}
            else:
                return {"x": x_list, "f(x)": fx_list}

        if i == iteration:
            return "Não existe raiz no intervalo com a configuração definida"
        else:
            return x

    except:
        if strike:
            return {}
        return "Erro, não foi possível achar a raiz"


def Secante(eq="", x=0, xi=0, e=0.01, strike=False, iteration=100):
    try:
        limpeza()
        i = 0
        """
        A função Secante é a implementação do método numérico de mesmo nome,
        retornando o valor de uma raiz aproximada, Ela apresenta os parâmetros:

        eq : string -> função matemática a ser calculada escrita em uma string;
        x : int/float -> chute inicial de uma raiz, geralmente um valor no
        intervalo de busca;
        xi : int/float -> outro chute de uma raiz, geralmente o outro valor no
        intervalo de busca;
        e : int/float -> precisão numérica da raiz aproximada;
        show : Bool -> Em breve.
        """
        x_list = []
        fx_list = []

        while i < iteration:
            fx = float(eval(eq))

            if strike:
                x_list.append(x)
                fx_list.append(fx)

            if abs(fx) < e:
                break
            else:
                fxi = float(eval(eq.replace("x", "xi")))
                xii = xi - ((fxi * (xi - x)) / (fxi - fx))

                x = xi
                xi = xii

            i += 1

        if strike:
            if i == iteration:
                return {}
            else:
                return {"x": x_list, "f(x)": fx_list}

        if i == iteration:
            return "Não existe raiz no intervalo com a configuração definida"
        else:
            return x
    except:
        if strike:
            return {}
        return "Erro, não foi possível achar a raiz"
