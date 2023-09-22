from spacy import load
nlp = load('pt_core_news_sm')

def lemmat(texto):
    doc = nlp(texto)

    lemmat_radicais = []

    for radicais in doc:
        lemmat_radicais.append(radicais.lemma_)
    
    texto_lemmat = ' '.join(lemmat_radicais)
    
    return texto_lemmat

print(lemmat("eu quero querer"))