faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

percentuais = {}

for estado,faturamento in faturamento_por_estado.items():
    percentual = (faturamento/faturamento_total)*100
    percentuais[estado]=percentual


print(f"Faturamento total da distribuidora: R${faturamento_total:.2f}")
print("\nPercentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
