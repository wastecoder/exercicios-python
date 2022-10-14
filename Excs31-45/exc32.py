fatorial = int(input("Digite o número do fatorial: "))
aux = fatorial

for contador in range(fatorial-1, 1, -1):
    # print(f"{fatorial} x {contador} = {fatorial*contador}")
    fatorial *= contador

print(f"Fatorial [{aux}!] = {fatorial}")
