# PROGRAMA DE REPRESENTACIÓN DE ESPACIO VECTORIAL
## Descripción
A partir del corpus del repositorio "corpus_normalized_data.csv" con las siguintes características:
- 362 noticias
- 6 columnas descriptivas, de las cuales se usan 2 (titulo y contenido)
- Noticias extraidas del canal RSS de La Jornada y La expansión en las secciones de deporte, ciencia y tecnología, economía y cultura.
Se obtienen representaciones de espacio vectorial, tomando en cuenta:
- Tamaño del n-grama (unigrama o bigrama)
- Tipo de representación (binaria, conteo de frecuencias o tf-idf)
- Contenido a usar para la búsqueda (titulo, descripción, o ambas)

El programa permite igualmente elegir un corpus propio, este debe estar en formato csv con tabuladores como separadores. Además, el csv debe tener 2 columnas con cabeceras "Title" y "Content" forzosamente.

Para realizar una prueba exhaustiva, es necesario colocar las pruebas en la carpeta Pruebas. Los archivos en esta carpeta deben ser TXT con una única línea que represente el query con el que se hará la prueba.

## Uso del programa
1. Establecer un entorno virtual
```
path/to/DocumentSimilarity> python -m venv venv
```
2. Instalar las librerías necesarias
```
path/to/DocumentSimilarity> pip install -m requirements.txt
```
Tambien se debe ejecutar un importe aidicional para un modelo de normalización, ya que se debe normalizar las cadenas de búsqueda *TODO*
3. Ejecutar el programa iniciando la interfaz de usuario y seguir las instrucciones
```
path/to/DocumentSimilarity> python Representaciones.py
```

