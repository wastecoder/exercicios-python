precoAtual = float(input("Digite o preço atual do produto: "))
mediaMensal = float(input("Digite o média mensal do produto: "))

if mediaMensal < 500 and precoAtual < 30:
    precoNovo = precoAtual * 1.1
    print(f"[1] Novo preço do produto [110%] >>> R${precoNovo}")
elif 500 <= mediaMensal < 1000 and 30 <= precoAtual < 80:
    precoNovo = precoAtual * 1.15
    print(f"[2] Novo preço do produto [115%] >>> R${precoNovo}")
elif mediaMensal >= 1000 and precoAtual >= 80:
    precoNovo = precoAtual * 0.95
    print(f"[3] Novo preço do produto [95%] >>> R${precoNovo}")
else:
    print(f"[4] Preço continua igual! [100%] >>> R${precoAtual}")
