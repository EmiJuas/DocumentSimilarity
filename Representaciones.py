import customtkinter as ctk
from tkinter import messagebox, filedialog
import subprocess
import os

# Variable global para almacenar la ruta del archivo
archivo_corpus = ""

# Función para seleccionar el archivo
def seleccionar_archivo():
    global archivo_corpus
    archivo_corpus = filedialog.askopenfilename(
        title="Seleccionar archivo corpus",
        filetypes=(("Archivos de texto", "*.csv"), ("Todos los archivos", "*.*"))
    )
    if archivo_corpus:
        label_archivo.configure(text=f"Archivo seleccionado: {os.path.basename(archivo_corpus)}")
        boton_crear.configure(state="normal")  # Habilitar el botón "Crear"

# Función que se ejecuta cuando se presiona el botón "Crear"
def crear_representaciones():
    if not archivo_corpus:
        messagebox.showwarning("Advertencia", "Debe seleccionar un archivo antes de continuar.")
        return
    
    try:
        # Llamar al script de vectorización pasando el archivo corpus como argumento
        subprocess.run(["python", "./vectorizacion.py", archivo_corpus], check=True)
        messagebox.showinfo("Éxito", "Representaciones vectoriales creadas correctamente.")
        
        # Cerrar la ventana actual antes de cargar la nueva interfaz
        app.destroy()
        
        # Ejecutar el archivo de la interfaz
        subprocess.run(["python", "./interfaz.py"], check=True)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")

# Configuración principal de la aplicación
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("Representaciones Vectoriales")

# Crear un texto de instrucciones
label_texto = ctk.CTkLabel(master=app, text="Seleccione un archivo corpus")
label_texto.pack(pady=20)

# Botón para seleccionar el archivo
boton_seleccionar = ctk.CTkButton(
    master=app,
    text="Seleccionar archivo",
    command=seleccionar_archivo
)
boton_seleccionar.pack(pady=10)

# Etiqueta para mostrar el archivo seleccionado
label_archivo = ctk.CTkLabel(master=app, text="Ningún archivo seleccionado")
label_archivo.pack(pady=10)

# Crear un botón que diga "Crear representaciones vectoriales" y desactivado inicialmente
boton_crear = ctk.CTkButton(
    master=app,
    text="Crear",
    command=crear_representaciones,
    state="disabled"  # Desactivado hasta que se seleccione un archivo
)
boton_crear.pack(pady=20)

# Iniciar la aplicación
app.mainloop()
