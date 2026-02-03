# Extends
def Extends(f, inf, sup, apro):
    """
    Calcula a solução exata da integral definida da função f no
    intervalo [inf, sup] e imprime a solução aproximada, solução exata,
    erro absoluto e erro relativo.

    Parâmetros:
    f (função): A função a ser integrada.
    inf (float): O limite inferior do intervalo de integração.
    sup (float): O limite superior do intervalo de integração.
    apro (float): A solução aproximada da integral.

    Retorna:
    None
    """
    from scipy import integrate

    # Calcula a solução exata
    exat = integrate.quad(f, inf, sup)[0]

    # Imprime os resultados
    print("--" * 15)
    print(f"Solução aproximada: {apro:>10.4f}")
    print(f"Solução exata: {exat:>15.4f}")
    print(f"Erro absoluto: {abs(exat - apro):>15.4f}")
    print(f"Erro relativo: {(abs(exat - apro)/exat)*100:>13.4f} %")
    print("--" * 15)


def tabela(listas=[], dicio={}, values=True):
    print(f'{"|":<}{"-=-"*26:^}{"|":>}')
    print(f'{"|":<}{dicio["função"] :^78}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')

    print(f'{"|":<}R**2= {dicio["R_quadrado"]:^12.4f}', end="")
    print(f'{"|":<}tam = {dicio["tamanho"]:^4}', end="")
    print(f'{"|":<}média y = {dicio["media_y"]:^10.4f}', end="")
    print(f'{"|":<}b = {dicio["b"]:^9.4f}', end="")
    print(f'{"|":<}a = {dicio["a"]:^9.4f}{"|":>}')

    print(f'{"|":<}{"-=-"*26:}{"|":>}')
    print(f'{"|":<}{"x":^12}', end="")
    print(f'{"|":<}{"y":^12}', end="")
    print(f'{"|":<}{"xy":^12}', end="")
    print(f'{"|":<}{"x**2":^12}', end="")
    print(f'{"|":<}{"sq_reg":^12}', end="")
    print(f'{"|":<}{"sq_tot":^13}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')

    if values:
        for i in range(dicio["tamanho"]):
            for j in range(0, len(listas)):
                print(f'{"|":<}{listas[j][i]:>12.4f}', end="")
            print(f'{"|":>2}')
        print(f'{"|":<}{"---"*26:}{"|":>}')

    print(f'{"|":<}{dicio["sum_x"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_y"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_xy"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_xquadrado"]:>12.4F}', end="")
    print(f'{"|":<}{dicio["sum_sq_regressão"]:>12.4f}', end="")
    print(f'{"|":<}{dicio["sum_sq_totais"]:>13.4f}{"|":>}')
    print(f'{"|":<}{"-=-"*26:}{"|":>}')
