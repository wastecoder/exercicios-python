tipoInvestimento = int(input("Digite o tipo de investimento [1/2]: "))
valorInvestimento = float(input("Digite o valor investido: (R$) "))

if tipoInvestimento == 1:
    print(f"30 dias na poupança [+3%] renderá [R${valorInvestimento * 1.03}]")
elif tipoInvestimento == 2:
    print(f"30 dias na renda fixa [+5%] renderá [R${valorInvestimento * 1.05}]")
else:
    print("Tipo de investimento inválido!")
