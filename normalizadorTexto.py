import pandas as pd
import stanza

config = {
    'processors': 'tokenize,mwt,pos,lemma',
    'lang': 'es'
}

nlp = stanza.Pipeline(**config)

def normalizarTexto(texto):
    try:
        doc = nlp(texto)
        cadenaNorm = ""
        for sent in doc.sentences:
            for token in sent.words:
                if token.pos not in {'ADP', 'CCONJ', 'DET', 'SCONJ', 'PRON'}:
                    cadenaNorm += token.lemma + " "
    except:
        cadenaNorm = ""

    return cadenaNorm



     