maior = 0
menor = 0

controlador = 1
while controlador < 4:
    numero = float(input(f"Digite o {controlador}º número inteiro positivo: "))

    if numero < 0 or numero % 1 != 0:
        print("ERRO: digite apenas inteiros positivos!")
        controlador -= 1
    else:
        numero = int(numero)
        if maior == 0 and maior == 0:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            elif numero < menor:
                menor = numero

    controlador += 1

print(f"\nMenor = {menor}\nMaior = {maior}")
