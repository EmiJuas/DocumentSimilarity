from predicion import Prediccion
import numpy as np

objeto_predicciones = Prediccion(Prediccion.BINARY, Prediccion.UNIGRAMA, Prediccion.TITULO)

print(objeto_predicciones.representacion)

print(objeto_predicciones.vectorizador)

query = ["OpenAI innovacion MEXICO "]
 
objeto_predicciones.predecir(query)