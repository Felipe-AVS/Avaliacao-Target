
faturamentoMensal = [
    {"estado" : "SP",
     "valor" : 67836.43},
    {"estado" : "RJ",
     "valor" : 36678.66},
    {"estado" : "MG",
     "valor" : 29229.88},
    {"estado" : "ES ",
     "valor" : 27165.48},
    {"estado" : "OUTROS",
     "valor" : 19849.53},
]

def calculoPorcentagens(faturamento):
    total = 0
    for estado in faturamento:
        total += estado['valor']

    for estado in faturamento:
        uf = estado['estado']
        porcentagem = (estado['valor'] / total) *100;
        print("O Estado de "+uf+" representa "+str(f"{porcentagem:.2f}")+"% do faturamento")
    print("O valor total do faturamento é de: "+str(total))

calculoPorcentagens(faturamentoMensal)

