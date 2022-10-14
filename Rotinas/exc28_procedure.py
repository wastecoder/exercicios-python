def promocao(preco_atual, media_mensal):
    print(f"Preço atual = {preco_atual} /// Média mensal = {media_mensal}")
    if media_mensal < 500 and preco_atual < 30:
        preco_novo = preco_atual * 1.1
        print(f"[1] Novo preço do produto [110%] >>> R${preco_novo}\n")
    elif 500 <= media_mensal < 1000 and 30 <= preco_atual < 80:
        preco_novo = preco_atual * 1.15
        print(f"[2] Novo preço do produto [115%] >>> R${preco_novo}\n")
    elif media_mensal >= 1000 and preco_atual >= 80:
        preco_novo = preco_atual * 0.95
        print(f"[3] Novo preço do produto [95%] >>> R${preco_novo}\n")
    else:
        print(f"[4] Preço continua igual! [100%] >>> R${preco_atual}\n")


promocao(20, 400)
promocao(60, 600)
promocao(90, 1200)
promocao(79, 1000)
