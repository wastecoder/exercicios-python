tempo = int(input("Digite o tempo do percurso (h): "))
velocidadeMedia = int(input("Digite a velocidade media do percurso (km/h): "))

distancia = tempo*velocidadeMedia

print(f"Com autonomia de 12km/l, andando à {velocidadeMedia}km/h por {tempo}h, gastou {distancia/12}l")
