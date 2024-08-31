




faturamento_sp = 67836.49
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
outros_estados = 19849.53
faturamento_total = sum([faturamento_sp, faturamento_es, faturamento_mg, faturamento_rj, outros_estados])

percentual_sp = (faturamento_sp / faturamento_total) * 100
percentual_rj = (faturamento_rj / faturamento_total) * 100
percentual_mg = (faturamento_mg / faturamento_total) * 100
percentual_es = (faturamento_es / faturamento_total) * 100
percentual_outros = (outros_estados / faturamento_total) * 100

print(f"Percentual de SP: {percentual_sp:.2f}%")
print(f"Percentual de RJ: {percentual_rj:.2f}%")
print(f"Percentual de MG: {percentual_mg:.2f}%")
print(f"Percentual de ES: {percentual_es:.2f}%")
print(f"Percentual de Outros: {percentual_outros:.2f}%")