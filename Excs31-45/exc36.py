numero = int(input("Digite o final da série (1/N!): "))
soma = 0
fatorial = 1

for contador in range(0, numero+1):
    for x in range(2, contador+1):
        # print(f"{fatorial} x {x} = {fatorial*x}")
        fatorial *= x

    soma += 1/fatorial
    fatorial = 1
    if contador == numero:
        print(f"1/{contador}!")
    else:
        print(f"1/{contador}! + ", end='')
    # print(f"1/{contador}! = {1/fatorial}")

print(f"\nSoma da série [{numero}] = {soma}")
