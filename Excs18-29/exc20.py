import math

valorA = int(input("Digite o coeficiente A: "))
valorB = int(input("Digite o coeficiente B: "))
valorC = int(input("Digite o coeficiente C: "))

delta = (valorB**2) - (4*valorA*valorC)

if delta > 0: #1, -5, 4 = {4, 1}
    delta = math.sqrt(delta)
    print(f"x1 = {((-valorB) + delta)/(2*valorA)}")
    print(f"x2 = {((-valorB) - delta)/(2*valorA)}")
elif delta == 0: #1, 6, 9 = {-3}
    print(f"x1 = x2 = {(-valorB)/(2*valorA)}")
else: #2, 2, 1 = {}
    print(f"Delta negativo ({delta}), logo não possui raiz!")
