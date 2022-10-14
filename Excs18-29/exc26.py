v1 = int(input("Digite o 1º número: "))
v2 = int(input("Digite o 2º número: "))

if v1 > v2 and v1 % v2 == 0:
    print(f"[1] {v1} é divisível por {v2}")
if v2 > v1 and v2 % v1 == 0:
    print(f"[2] {v2} é divisível por {v1}")
