import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwordsdic = stopwords.words('portuguese')

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('word_tokenize')

def stopwords(texto):
    
    palavras = word_tokenize(texto, language='portuguese') # Tokenize é analisar palavras individualmente, basicamente
    
    palavras_sem_stopword = []
    
    for palavra in palavras:
        if palavra not in stopwordsdic:
            palavras_sem_stopword.append(palavra)
    
    # Reúna as palavras sem stopwords em uma string novamente
    texto_sem_stopword = ' '.join(palavras_sem_stopword)
    
    return texto_sem_stopword

ex = 'eu gosto muito de a minha maçã'
ex_sem_stopwords = stopwords(ex)
print(stopwords(ex))