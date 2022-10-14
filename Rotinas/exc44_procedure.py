def potencia(base=1, expoente=0):
    res = 1
    for controlador in range(1, expoente+1):
        res *= base

    print(f"{base}^{expoente} = {res}\n")


potencia()
potencia(5, 2)
potencia(5, 3)
