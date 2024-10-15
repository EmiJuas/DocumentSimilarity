import customtkinter as ctk
from tkinter import messagebox
import subprocess
import os

# Función que se ejecuta cuando se presiona el botón
def crear_representaciones():
    try:
        # Llamar al script de vectorización
        subprocess.run(["python", "./vectorizacion.py"], check=True)
        messagebox.showinfo("Éxito", "Representaciones vectoriales creadas correctamente.")
        
        # Cerrar la ventana actual antes de cargar la nueva interfaz
        app.destroy()
        
        # Ejecutar el archivo de la interfaz
        subprocess.run(["python", "./interfaz.py"], check=True)

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar el script: {e}")

# Configuración principal de la aplicación
ctk.set_appearance_mode("dark")  # Modos: "System" (por defecto), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas de color: "blue" (por defecto), "green", "dark-blue"

app = ctk.CTk()  # Crear la ventana principal
app.geometry("400x200")  # Tamaño de la ventana
app.title("Representaciones Vectoriales")  # Título de la ventana

# Crear un texto encima del botón
label_texto = ctk.CTkLabel(master=app, text="Crear representaciones vectoriales")
label_texto.pack(pady=20)  # Posicionar el texto con un margen vertical

# Crear un botón que diga "Crear representaciones vectoriales"
boton_crear = ctk.CTkButton(
    master=app,
    text="Crear",
    command=crear_representaciones  # Llamada a la función cuando se presiona el botón
)
boton_crear.pack(pady=20)  # Posicionar el botón con un margen vertical

# Iniciar la aplicación
app.mainloop()