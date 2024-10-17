from predicion import Prediccion
from normalizadorTexto import normalizarTexto
import pandas as pd
from interfaz import objeto_predicciones, archivo_seleccionado  # Importar desde interfaz.py

# Verificar que se ha seleccionado un archivo en la interfaz

print("golman")

if archivo_seleccionado:
    with open(archivo_seleccionado, 'r') as file:
        query = [file.read()]
else:
    query = ["Pepe pecas pica papas con un pico"]

# Normalizar el texto del query
query[0] = normalizarTexto(query[0])

# Predecir con el objeto_predicciones creado en la interfaz
top10 = objeto_predicciones.predecir(query)
df = pd.read_csv(r'.\\corpus_raw_data.csv', sep='\t')
titulos = df['Title']

# Imprimir los resultados
for noticia in top10:
    (indice, similitud) = noticia
    print(f"{titulos[indice]} : {similitud}")