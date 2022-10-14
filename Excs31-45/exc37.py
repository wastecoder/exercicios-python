numero = int(input("Digite a quantidade de elementos de Fibonacci: "))

primeiro = 0
segundo = 1

# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3

for controlador in range(1, numero+1):
    print(f"{controlador}º elemento: {segundo}")
    res = primeiro + segundo
    primeiro = segundo
    segundo = res
