import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            messagebox.showerror("Error", "La longitud debe ser un número positivo.")
            return
        contraseña = ''.join(secrets.choice(string.printable.strip()) for _ in range(longitud))
        label_contraseña.config(text="Contraseña generada: " + contraseña)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para la longitud.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

# Etiqueta y entrada para la longitud de la contraseña
label_longitud = tk.Label(root, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)

# Botón para generar la contraseña
boton_generar = tk.Button(root, text="Generar Contraseña", command=generar_contraseña)
boton_generar.pack(pady=10)

# Etiqueta para mostrar la contraseña generada
label_contraseña = tk.Label(root, text="Contraseña generada: ")
label_contraseña.pack(pady=5)

# Ejecuta la ventana principal
root.mainloop()
