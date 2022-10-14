final = int(input("Digite o final da série (1/N): "))
soma = 0

for controlador in range(1, final + 1):
    soma += 1 / controlador
    if controlador == final:
        print(f"1/{controlador}")
    else:
        print(f"1/{controlador} + ", end='')

print("\nSoma da série = ", soma)
