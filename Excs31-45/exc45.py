soma = 0
final = 15

for contador in range(1, final+1):
    if contador == 1: #Primeiro elemento da série
        print(f"{contador}/{contador**2}", end='')
        soma += contador/(contador**2)
    elif contador % 2 != 0: #Ímpares da série (+)
        soma += contador/(contador**2)
        print(f" + {contador}/{contador**2}", end='')
    else: #Pares da série (-)
        soma -= contador/(contador**2)
        print(f" - {contador}/{contador**2}", end='')

print("\n\nSérie = 1 – 2/4 + 3/9 – 4/16 + 5/25 - ...")
print(f"Soma da série [{final}] = {soma}")
