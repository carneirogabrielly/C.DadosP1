def verifica_performance(planilha_limpa):

    count_comparativo = (planilha_limpa['Acionável/Direcionável/Não Acionável'] == ['Classificador Automático']).sum() # Conta quantos valores nas duas são correspondentes
    total_elementos = len(planilha_limpa) #Total de linhas

    porcentagem_concordancia = (count_comparativo / total_elementos) * 100
    
    return 'Há {0}% de concordância entre a classificação manual e automática'.__format__(porcentagem_concordancia)