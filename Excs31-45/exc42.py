final = 50
soma = 0

for contador in range(1, final+1):
    # print(f"{contador}/{(contador*2)-1} + ", end='')
    print(f"{contador}/{(contador*2)-1} = {contador/((contador*2)-1)}")
    soma += contador/((contador*2)-1)


print("\nSérie = 1/1 + 2/3 + 3/5 + 4/7 + ...")
print(f"Soma da série [{final}] = {soma}")
