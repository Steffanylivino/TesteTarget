import json 

arquivo_json = "dados.json"

def analisar_faturamento(arquivo_json):
    with open(arquivo_json,"r") as file:
        dados=json.load(file)

    valores = [dia["valor"]for dia in dados if dia["valor"]>0]

    menor_valor = min(valores)if valores else 0
    maior_valor = max(valores) if valores else 0 
    media_mensal = sum(valores)/len(valores) if valores else 0 
    dias_acima_da_media = sum (1 for valor in valores if valor>media_mensal)

    return {
        "menor_valor":menor_valor,
        "maior_valor":maior_valor,
        "media_mensal":media_mensal,
        "dias_acima_da_media":dias_acima_da_media

    }    

resultado = analisar_faturamento(arquivo_json)

print(f"Menor valor de faturamento: R${resultado['menor_valor']:.2f}")
print(f"Maior valor de faturamento: R${resultado['maior_valor']:.2f}")
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_da_media']}")