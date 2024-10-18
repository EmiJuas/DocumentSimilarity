from predicion import Prediccion
from normalizadorTexto import normalizarTexto
import pandas as pd
import os.path

carpeta = "./Pruebas"

objetos_pred = []
for nom_arch in os.listdir(carpeta):
    top_global = []
    ruta_arch = os.path.join(carpeta, nom_arch)
    texto = ""
    if os.path.isfile(ruta_arch):
        with open(ruta_arch, 'r', encoding='utf-8') as arch:
            texto = arch.readline().strip()
    query = [texto]
    query[0] = normalizarTexto(query[0])
    for representacion in [Prediccion.BINARY, Prediccion.CUNTER, Prediccion.TF_IDF]:
        for n_grama in [Prediccion.UNIGRAMA, Prediccion.BIGRAMA]:
            for espacio_busq in [Prediccion.TITULO, Prediccion.CONTENIDO, Prediccion.TITULO_CONTENIDO]:
                objeto_pred = Prediccion(representacion, n_grama, espacio_busq)
                top10 = objeto_pred.predecir(query)
                for noticia in top10:
                    indice, similitud = noticia
                    top_global.append((indice+2, representacion, n_grama, espacio_busq, similitud))
    
    print(texto)
    print("CorpInd\tRepres\tN-Grama\tElemento\tSimilitud")
    top_global.sort(reverse=True, key=lambda x: x[4])
    for i in range(10):
        tupla = top_global[i]
        print(f"{tupla[0]}\t{tupla[1]}\t{tupla[2]}\t{tupla[3]}\t{tupla[4]}")
    print("\n\n")
