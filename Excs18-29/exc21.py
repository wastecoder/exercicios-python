nota1 = int(input("Digite a 1ª nota: "))
nota2 = int(input("Digite a 2ª nota: "))
nota3 = int(input("Digite a 3ª nota: "))
nota4 = int(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print("Média = ", media)

if media >= 6:
    print("Aprovado!")
elif media >= 3:
    print("Exame!")
else:
    print("Retido!")
