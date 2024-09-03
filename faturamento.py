import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

faturamento_positivo = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(faturamento_positivo)

maior_faturamento = max(faturamento_positivo)

media = sum(faturamento_positivo)/ len(faturamento_positivo)

ganho_superior_media = len([valor for valor in faturamento_positivo if valor > media])
print('-'*30)
print(f"O menor faturamento foi R$ {menor_faturamento:.2f}")
print('-'*30)
print(f"O maior faturamento foi R$ {maior_faturamento:.2f}")
print('-'*30)
print(f"Tivemos {ganho_superior_media} dias que o faturamento foi superior a média")

