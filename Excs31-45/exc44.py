base = int(input("Digite a base da potência: "))
expoente = int(input("Digite o expoente da potência: "))

res = 1
for controlador in range(1, expoente+1):
    res *= base

print(f"{base}^{expoente} = {res}")
