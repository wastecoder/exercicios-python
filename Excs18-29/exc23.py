v1 = int(input("Digite o 1º valor (ordem crescente): "))
v2 = int(input("Digite o 2º valor (ordem crescente): "))
v3 = int(input("Digite o 3º valor (ordem crescente): "))
v4 = int(input("Digite o 4º valor: "))

if v4 <= v1:
    print(f"[1] {v4} >>> {v1} >>> {v2} >>> {v3}")
elif v4 <= v2:
    print(f"[2] {v1} >>> {v4} >>> {v2} >>> {v3}")
elif v4 <= v3:
    print(f"[3] {v1} >>> {v2} >>> {v4} >>> {v3}")
else:
    print(f"[4] {v1} >>> {v2} >>> {v3} >>> {v4}")
