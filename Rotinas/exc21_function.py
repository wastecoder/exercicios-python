def media_escolar(n1, n2, n3, n4):
    media = (n1 + n1 + n3 + n4) / 4
    if media >= 6:
        return "Aprovado!"
    elif media >= 3:
        return "Exame!"
    else:
        return "Retido!"


print(media_escolar(6, 6, 6, 6))
print(media_escolar(6, 6, 6, 5))
print(media_escolar(3, 3, 3, 2))
