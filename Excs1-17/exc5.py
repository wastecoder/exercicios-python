import math

valorA = int(input("Digite o coeficiente A: "))
valorB = int(input("Digite o coeficiente B: "))
valorC = int(input("Digite o coeficiente C: "))

delta = (valorB**2) - (4 * valorA * valorC)
delta = math.sqrt(delta)

x1 = (-valorB + delta) / (2 * valorA)
x2 = (-valorB - delta) / (2 * valorA)

print(f"\nx1 = {x1}\nx2 = {x2}")
