from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import pandas as pd
import os.path
import pickle

# Verificar si se pasó el archivo corpus como argumento
if len(sys.argv) != 2:
    print("Uso: python vectorizacion.py <ruta_al_archivo_corpus>")
    sys.exit(1)

# Leer la ruta del archivo corpus desde los argumentos de línea de comandos
archivo_corpus = sys.argv[1]

# Verificar si el archivo existe
if not os.path.exists(archivo_corpus):
    print(f"El archivo {archivo_corpus} no existe.")
    sys.exit(1)

# Leer el archivo corpus
df = pd.read_csv(archivo_corpus, sep='\t')

if not os.path.exists('./representaciones'):
    os.makedirs('./representaciones')

titulos = df['Title'].fillna('')
contenidos = df['Content'].fillna('')
titulos_contenidos = []

#concatenar titulo y contenido para la ultima representacion
for i, titulo in enumerate(titulos):
    cont = contenidos[i]
    if cont != '':
        titulos_contenidos.append(str(titulo) + " " + str(cont))
    else:
        titulos_contenidos.append(titulo)

def guardaPickle(X, nombre):
    nombreArch = './representaciones/X_vect_' + nombre + '.pkl'
    if (os.path.exists(nombreArch)):
        print ('Ya existe')
        with open(nombreArch, 'rb') as f:
            pickle.load(f)
            f.close()
    else:
        with open(nombreArch, 'wb') as f:
            pickle.dump(X, f)
            f.close()

def vecotrs(tipo, tupla):
    if tipo == 'frec':
        vectorizador = CountVectorizer(token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=tupla)
    elif tipo == 'tfidf':
        vectorizador = TfidfVectorizer(token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=tupla)
    else:
        vectorizador = CountVectorizer(binary=True, token_pattern= r'(?u)\w+|\w+\n|\.|\¿|\?', ngram_range=tupla)

    return vectorizador

arreglos = [titulos, contenidos, titulos_contenidos]
for i, name in enumerate(['title', 'cont', 'title-cont']):
    corpus = arreglos[i]
    for tupla in [(1,1), (2,2)]:
        for tipo in ['frec', 'bin', 'tfidf']:
            vectorizador = vecotrs(tipo, tupla)
            X = vectorizador.fit_transform(corpus)
            #se guarda en el archivo la representación y el vecortizado que la orignó
            tupla_a_guardar = (X, vectorizador)
            guardaPickle(tupla_a_guardar, str(name) + '_' + str(tupla) + '_' + tipo)
            print(str(i) + '_' + str(tupla) + '_' + tipo + ' guardado')