import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox

# Función para abrir el diálogo de selección de archivo
def cargar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
    )
    if archivo:
        label_archivo.configure(text=f"Archivo seleccionado: {archivo}")  # Actualizar etiqueta con el archivo seleccionado
    else:
        label_archivo.configure(text="No se seleccionó ningún archivo.")  # Mensaje si no se seleccionó archivo

# Configuración principal de la aplicación
ctk.set_appearance_mode("dark")  # Modos: "System" (por defecto), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas de color: "blue" (por defecto), "green", "dark-blue"

app = ctk.CTk()  # Crear la ventana principal
app.geometry("400x450")  # Tamaño de la ventana
app.title("Document Similarity")  # Título de la ventana

# Crear un contenedor para alinear el texto y el botón horizontalmente
frame_contenedor = ctk.CTkFrame(master=app)
frame_contenedor.pack(pady=20)

# Etiqueta de texto
etiqueta = ctk.CTkLabel(master=frame_contenedor, text="Archivo de prueba:")
etiqueta.pack(side="left", padx=15)  # Posicionar a la izquierda con un espacio

# Crear un botón para cargar archivos
boton_cargar = ctk.CTkButton(
    master=frame_contenedor,
    text="Cargar Archivo",
    command=cargar_archivo  # Llamada a la función cuando se presiona el botón
)
boton_cargar.pack(side="left", padx=15)  # Posicionar a la derecha de la etiqueta

# Etiqueta para mostrar el archivo seleccionado
label_archivo = ctk.CTkLabel(master=app, text="No se ha seleccionado ningún archivo.")
label_archivo.pack(pady=20)  # Posicionar debajo del botón

# Crear un solo contenedor para "Características" y "Tipo"
frame_opciones = ctk.CTkFrame(master=app)
frame_opciones.pack(pady=10)

# Primer renglón: Etiqueta y menú desplegable para "Características"
label_caracteristicas = ctk.CTkLabel(master=frame_opciones, text="Características:")
label_caracteristicas.pack(side="top", anchor="w", padx=15, pady=5)  # Alinear a la izquierda y dar un pequeño margen

opciones_caracteristicas = ctk.StringVar(value="Unigramas")  # Valor por defecto
menu_caracteristicas = ctk.CTkOptionMenu(
    master=frame_opciones,
    variable=opciones_caracteristicas,
    values=["Unigramas", "Bigramas"]
)
menu_caracteristicas.pack(side="top", anchor="w", padx=15)  # Alinear a la izquierda

# Segundo renglón: Etiqueta y menú desplegable para "Representación"
label_tipo = ctk.CTkLabel(master=frame_opciones, text="Representación:")
label_tipo.pack(side="top", anchor="w", padx=15, pady=5)  # Alinear a la izquierda

opciones_representacion = ctk.StringVar(value="Frecuencia")  # Valor por defecto
menu_tipo = ctk.CTkOptionMenu(
    master=frame_opciones,
    variable=opciones_representacion,
    values=["Frecuencia", "Binario", "TF-IDF"]
)
menu_tipo.pack(side="top", anchor="w", padx=15)  # Alinear a la izquierda

# Tercer renglón: Etiqueta y menú desplegable para "Elemento de comparación"
label_elemento = ctk.CTkLabel(master=frame_opciones, text="Elemento de comparación:")
label_elemento.pack(side="top", anchor="w", padx=15, pady=5)  # Alinear a la izquierda

opciones_elemento = ctk.StringVar(value="Titulo")  # Valor por defecto
menu_elemento = ctk.CTkOptionMenu(
    master=frame_opciones,
    variable=opciones_elemento,
    values=["Titulo", "Contenido", "T+C"]
)
menu_elemento.pack(side="top", anchor="w", padx=15, pady=5)  # Alinear a la izquierda

# Agregar un botón al final
boton_final = ctk.CTkButton(
    master=app,
    text="Procesar",
    command=lambda: messagebox.showinfo("Procesando", "Se ha iniciado el proceso")
)
boton_final.pack(pady=20)  # Posicionar el botón al final con un margen de 20 píxeles

# Iniciar la aplicación
app.mainloop()