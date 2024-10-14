from predicion import Prediccion
from normalizadorTexto import normalizarTexto
import pandas as pd


objeto_predicciones = Prediccion(Prediccion.BINARY, Prediccion.UNIGRAMA, Prediccion.TITULO)

df = pd.read_csv(r'.\corpus_raw_data.csv', sep='\t')

titulos = df['Title']

query = ["Pepe pecas pica papas con un pico"]
query[0] = normalizarTexto(query[0])
 
top10 = objeto_predicciones.predecir(query)
for noticia in top10:
    (indice, similitud) = noticia
    print(f"{titulos[indice]} : {similitud}")