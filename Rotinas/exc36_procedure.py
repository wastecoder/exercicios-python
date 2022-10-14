def fatorial(valor=0):
    fatorial = 1
    for x in range(2, valor+1):
        # print(f"{fatorial} x {x} = {fatorial*x}")
        fatorial *= x

    return fatorial


def soma_serie(final=0):
    soma = 0
    for contador in range(0, final+1):
        fatorial_retorno = fatorial(contador)

        soma += 1 / fatorial_retorno
        print(f"1/{contador}! = {1 / fatorial_retorno}")
        # print(f"{contador}! = {fatorial_retorno}")

    print(f"Soma da série [{final}] = {soma}\n")


soma_serie(2)
soma_serie(3)
soma_serie()
print(fatorial())
