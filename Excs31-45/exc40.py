n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

for controlador in range(n1, n2+1):
    divisores = 0
    for primo in range(controlador, 0, -1):

        if divisores > 2 or (controlador % 2 == 0 and controlador != 2):
            break
        elif controlador % primo == 0:
            # print(f"{controlador}/{primo}")
            divisores += 1

    if divisores == 2:
        print(f"{controlador}, ", end='')
