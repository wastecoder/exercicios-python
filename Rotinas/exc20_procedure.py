import math


def equacao_segundo_grau(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    print(f"A = {a} /// B = {b} /// C = {c} /// DELTA = {delta}")

    if delta > 0:
        delta = math.sqrt(delta)
        print(f"x1 = {((-b) + delta) / (2 * a)}")
        print(f"x2 = {((-b) - delta) / (2 * a)}\n")
    elif delta == 0:
        print(f"x1 = x2 = {(-b) / (2 * a)}\n")
    else:
        print(f"Delta negativo ({delta}), logo não possui raiz!\n")


equacao_segundo_grau(1, -5, 4)
equacao_segundo_grau(1, 6, 9)
equacao_segundo_grau(2, 2, 1)
