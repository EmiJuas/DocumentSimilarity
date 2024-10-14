"""
Archivo que solo se encarga de hacer las prediciones,
para que sea utilizado por el script de pruebas
y para el script de interfaz que quiere el profe
y una que otra funcion auxiliar

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os.path
import math 
import numpy as np

#la clase se usa mayormente estatica
class Prediccion:

    #tipo representacion
    BINARY = 'bin'
    CUNTER = 'frec'
    TF_IDF = 'tfidf'

    #tamaño n-grama
    UNIGRAMA = '(1, 1)'
    BIGRAMA = '(2, 2)'

    #contenido a usar para la busqueda (el espacio de búsqueda)
    TITULO = 'title'
    CONTENIDO = 'cont'
    TITULO_CONTENIDO = 'title-cont'

    representacion = None
    vectorizador = None

    #constructor vacio, por si se quiere usar puro actualizar
    def __init__(self):
        pass

    def __init__(self, tipo_representacion, n_grama_usar, espacio_busqueda):
        detalles_representacion = self.obtener_representacion(tipo_representacion, n_grama_usar, espacio_busqueda)
        if detalles_representacion == None:
            print("\tNo se logró obtner la representacion")
            return
        (self.representacion, self.vectorizador) = detalles_representacion

    #para no ir creando objetos a cada rato, pues que solo se actualizen los datos
    def actualizar_representacion(self, tipo_representacion, n_grama_usar, espacio_busqueda):
        detalles_representacion = self.obtener_representacion(tipo_representacion, n_grama_usar, espacio_busqueda)
        if detalles_representacion == None:
            print("\tNo se logró obtner la representacion")
            return
        (self.representacion, self.vectorizador) = detalles_representacion

    #Usar las constantes de la clase para los arugmentos
    def obtener_representacion(self, tipo_representacion, n_grama_usar, espacio_busqueda):
        #se obtiene la ruta
        archivo_representacion = f"./representaciones/X_vect_{espacio_busqueda}_{n_grama_usar}_{tipo_representacion}.pkl"
        print(f"Busco el archivo: {archivo_representacion}")
        #se empieza a chambear
        try:
            if (os.path.exists(archivo_representacion)):
                print ('Existe el archivo de la representación')
                with open(archivo_representacion, 'rb') as f:
                    return pickle.load(f)
            else:
                print("No se encontró la representación deseada, ejecute la vectorización primero")
                return None #falsos para futuras verificaciones
        except EOFError as eofe:
            print(f"El archivo está vacío o corrupto: {eofe}")
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
        return None #se se llega aquí es por que no se obtuvo nada
        
    #función para Predecir
    def predecir(self,query):
        similitud = 0
        top10 = {}
        representacion_query = self.vectorizador.transform(query)
        print(representacion_query)
        for noticia in self.representacion.toarray():
            #se ingresó como arreglo para transform, así que se obtiene el unico registro
            print(f"Se parece a: {self.cosine(noticia, representacion_query.toarray()[0])}")
        #similitud = self.cosine(self.representacion.toarray(),representacion_query.toarray())
        return similitud
    
    #similitud coseno
    def cosine(self, x, y):
        val = sum(x[index] * y[index] for index in range(len(x)))
        sr_x = math.sqrt(sum(x_val**2 for x_val in x))
        sr_y = math.sqrt(sum(y_val**2 for y_val in y))
        res = val/(sr_x*sr_y)
        return (res)
 