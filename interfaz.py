import customtkinter as ctk
import pandas as pd
from tkinter import filedialog
from predicion import Prediccion
from normalizadorTexto import normalizarTexto
import os  # Para obtener solo el nombre del archivo

# Definir la variable global para la instancia de Prediccion
objeto_predicciones = None
archivo_seleccionado = None

# Función para abrir el diálogo de selección de archivo
def cargar_archivo():
    global archivo_seleccionado
    archivo_seleccionado = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo_seleccionado:
        archivo_nombre = os.path.basename(archivo_seleccionado)  # Obtener solo el nombre del archivo
        label_archivo.configure(text=f"Archivo seleccionado: {archivo_nombre}")  # Actualizar etiqueta
    else:
        label_archivo.configure(text="No se seleccionó ningún archivo.")

# Función para crear la instancia de Prediccion
def crear_prediccion():
    global objeto_predicciones
    caracteristicas = menu_caracteristicas.get()
    representacion = menu_tipo.get()
    elemento = menu_elemento.get()

    if caracteristicas == "Unigramas":
        caracteristicas_valor = Prediccion.UNIGRAMA
    else:
        caracteristicas_valor = Prediccion.BIGRAMA

    if representacion == "Frecuencia":
        representacion_valor = Prediccion.CUNTER
    elif representacion == "Binario":
        representacion_valor = Prediccion.BINARY
    else: 
        representacion_valor = Prediccion.TF_IDF

    if elemento == "Titulo":
        elemento_valor = Prediccion.TITULO
    elif elemento == "Contenido":
        elemento_valor = Prediccion.CONTENIDO
    else:
        elemento_valor = Prediccion.TITULO_CONTENIDO

    # Crear instancia de Prediccion y asignarla a la variable global
    objeto_predicciones = Prediccion(representacion_valor, caracteristicas_valor, elemento_valor)
    
    if archivo_seleccionado:
        with open(archivo_seleccionado, 'r') as file:
            query = [file.read()]
    else:
        query = ["Pepe pecas pica papas con un pico"]

    # Normalizar el texto del query
    query[0] = normalizarTexto(query[0])

    # Predecir con el objeto_predicciones creado en la interfaz
    top10 = objeto_predicciones.predecir(query)

    # Limpiar la tabla antes de mostrar nuevos resultados
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # Mostrar los resultados en la tabla
    for i, noticia in enumerate(top10):
        (indice, similitud) = noticia
        sim_text = f"{similitud:}"
        
        # Crear y posicionar las etiquetas de cada fila en la tabla
        ctk.CTkLabel(frame_resultados, text=f"{i+1}. Índice {indice+2}", anchor="w").grid(row=i, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkLabel(frame_resultados, text=sim_text, anchor="e").grid(row=i, column=1, padx=10, pady=5, sticky="e")

# Crear la ventana principal
root = ctk.CTk()
root.geometry("730x450")  # Ajustar tamaño de la ventana

ctk.set_appearance_mode("dark")  # Modos: "System" (por defecto), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas de color: "blue" (por defecto), "green", "dark-blue"

# Configurar el grid del root para centrar el contenido
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Crear un frame para contener y centrar los widgets
frame_central = ctk.CTkFrame(root)
frame_central.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Configurar el grid del frame central para centrar los widgets
frame_central.grid_columnconfigure(0, weight=1)
frame_central.grid_rowconfigure(0, weight=1)

# Crear los frames para la organización dentro del frame central
frame_opciones = ctk.CTkFrame(frame_central)
frame_opciones.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame_resultados = ctk.CTkFrame(frame_central)
frame_resultados.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# --- Sección de opciones centrada ---
# Etiquetas y menús desplegables

# Etiqueta y menú para "Característica"
label_caracteristicas = ctk.CTkLabel(frame_opciones, text="Característica:")
label_caracteristicas.grid(row=0, column=0, padx=10, pady=10, sticky="e")
menu_caracteristicas = ctk.CTkComboBox(frame_opciones, values=["Unigramas", "Bigramas"])
menu_caracteristicas.grid(row=0, column=1, pady=10, sticky="nsew")

# Etiqueta y menú para "Representación"
label_tipo = ctk.CTkLabel(frame_opciones, text="Representación:")
label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
menu_tipo = ctk.CTkComboBox(frame_opciones, values=["Frecuencia", "Binario", "TF-IDF"])
menu_tipo.grid(row=1, column=1, pady=10, sticky="nsew")

# Etiqueta y menú para "Elemento de comparación"
label_elemento = ctk.CTkLabel(frame_opciones, text="Elemento de comparación:")
label_elemento.grid(row=2, column=0, padx=10, pady=10, sticky="e")
menu_elemento = ctk.CTkComboBox(frame_opciones, values=["Titulo", "Contenido", "T+C"])
menu_elemento.grid(row=2, column=1, pady=10, sticky="nsew")

# Crear el widget label_archivo para mostrar el archivo seleccionado
label_archivo = ctk.CTkLabel(frame_opciones, text="No se seleccionó ningún archivo.")
label_archivo.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

# Botón para cargar el archivo
boton_cargar = ctk.CTkButton(frame_opciones, text="Cargar archivo", command=cargar_archivo)
boton_cargar.grid(row=4, column=0, columnspan=2, pady=20, sticky="nsew")

# Botón para procesar la información
boton_procesar = ctk.CTkButton(frame_opciones, text="Procesar", command=crear_prediccion)
boton_procesar.grid(row=5, column=0, columnspan=2, pady=20, sticky="nsew")

# Ejecutar la ventana
root.mainloop()
