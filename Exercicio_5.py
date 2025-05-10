def inverteTexto(texto):
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    print(texto + " -- "+ invertida)

inverteTexto("Teste")
