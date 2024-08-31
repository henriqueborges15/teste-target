import json

faturamento_json =''' [
    
    {"dia": 1, "valor": 1000.0},
    {"dia": 2, "valor": 1500.0},
    {"dia": 3, "valor": 3000.0},  
    {"dia": 4, "valor": 5000.0},   
    {"dia": 5, "valor": 2000.0},
    {"dia": 6, "valor": 0.0}, 
    {"dia": 7, "valor": 0.0}, 
    {"dia": 8, "valor": 0.0}, 
    {"dia": 9, "valor": 1200.0},
    {"dia": 10, "valor": 4000.0},
    {"dia": 11, "valor": 2000.0},
    {"dia": 12, "valor": 2500.0},
    {"dia": 13, "valor": 0.0},
    {"dia": 14, "valor": 0.0},
    {"dia": 15, "valor": 4000.0},
    {"dia": 16, "valor": 3500.0},
    {"dia": 17, "valor": 2500.0},
    {"dia": 18, "valor": 1000.0},
    {"dia": 19, "valor": 2500.0},
    {"dia": 20, "valor": 0.0},
    {"dia": 21, "valor": 0.0},
    {"dia": 22, "valor": 3500.0},
    {"dia": 23, "valor": 5500.0},
    {"dia": 24, "valor": 0.0},
    {"dia": 25, "valor": 2350.0},
    {"dia": 26, "valor": 3250.0},
    {"dia": 27, "valor": 0.0},
    {"dia": 28, "valor": 0.0},
    {"dia": 29, "valor": 5000.0},
    {"dia": 30, "valor": 1350.0}

]
'''

faturamento_por_dia = json.loads(faturamento_json)

faturamento_positivo = [dia['valor'] for dia in faturamento_por_dia if dia['valor'] > 0]

menor_faturamento = min(faturamento_positivo)

maior_faturamento = max(faturamento_positivo)

media = sum(faturamento_positivo)/ len(faturamento_positivo)

ganho_superior_media = len([valor for valor in faturamento_positivo if valor > media])

print(f"O menor faturamentio foi {menor_faturamento}")
print(f"O maior faturamentio foi {maior_faturamento}")
print(f"Os dias que o faturamentio foi acima da média: {ganho_superior_media}")

