dados_originais = [10, 20, 30]
dados_referencia = dados_originais
dados_copia = [10, 20, 30]

print(f"Dados Originais{dados_originais} é o mesmo objeto que Dados Referencia{dados_referencia}? {dados_originais is dados_referencia}")
print(f"Dados Originais{dados_originais} não é o mesmo objeto que Dados Cópia{dados_copia}? {dados_originais is not dados_copia}")