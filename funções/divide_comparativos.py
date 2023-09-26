def divide_comparativos(planilha):

    planilha = classifica_planilha(planilha)
    comparador = pd.crosstab(planilha['Classificador Automático'], planilha['Acionável/Direcionável/Não Acionável'],normalize=True, margins=True)

    pct_verdadeiros_positivos = comparador.iloc[0]['A'] + comparador.iloc[1]['D'] + comparador.iloc[2]['N'] 

    pct_falsos_A = comparador.iloc[0]['D'] + comparador.iloc[0]['N']
    pct_falsos_D = comparador.iloc[1]['A'] + comparador.iloc[1]['N']
    pct_falsos_N = comparador.iloc[2]['D'] + comparador.iloc[2]['A']

    return pct_verdadeiros_positivos*100, pct_falsos_A*100, pct_falsos_D*100, pct_falsos_N*100, comparador

verdadeiros_positivos = divide_comparativos(train,test)[0]
falsos_acionaveis = divide_comparativos(train,test)[1]
falsos_direcionaveis = divide_comparativos(train,test)[2]
falsos_nao_acionaveis = divide_comparativos(train,test)[3]
tabela_comparadora = divide_comparativos(train,test)[4]