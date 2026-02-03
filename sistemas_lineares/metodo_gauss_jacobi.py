# Método_de_Gauss_Jacobi
def Gauss_Jacobi(a=[], b=[], e=0.05):
    """
    Realiza o método iterativo de Gauss-Jacobi para resolver um sistema linear
    na forma matricial AX = B.

    Parâmetros de entrada:
    a: lista de listas representando a matriz A do sistema linear
    b: lista representando a matriz B do sistema linear
    e: critério de parada, representando a tolerância para a convergência

    Saída:
    Retorna a lista com a solução do sistema linear X.
    """
    size = len(a)
    x_anterior = [1] * size
    x_atual = [1] * size
    aux_m = [1] * size
    aux = maior = 0

    for k in range(size):
        x_anterior[k] = b[k] / a[k][k]

    while True:
        for i in range(size):
            for j in range(size):
                if i != j:
                    aux += -a[i][j] * x_anterior[j]

                    # O que está acontecendo é a operação: -a * x_{n} de cada
                    # sistema, um de cada vez e sendo armazenado.

            x_atual[i] = 1 / a[i][i] * (b[i] + aux)
            aux = 0

        for m in range(size):
            aux_m[m] = abs(x_atual[m] - x_anterior[m])

            if abs(x_atual[m]) > maior:
                maior = abs(x_atual[m])

        max_distance_rel = max(aux_m) / maior
        maior = 0

        # i = 0
        # print(f'soluçao {i+1}', x_atual)
        # print(f'Distância relativa: ', max_distance_rel)
        # i += 1

        if max_distance_rel < e:
            return x_atual
        else:
            x_anterior = x_atual[:]
