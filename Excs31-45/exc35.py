n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
soma = 0

if n1 > n2:
    aux = n1
    n1 = n2
    n2 = aux

for controlador in range(n1, n2 + 1):
    if controlador % 2 != 0:
        print(controlador)
        soma += controlador

print(f"Soma dos ímpares entre {n1} e {n2} = {soma}")
