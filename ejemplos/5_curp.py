import tkinter as tk
from tkinter import ttk, messagebox
import re

# Función para generar un CURP básico
def generar_curp():
    nombre = entrada_nombre.get().upper()
    apellido_paterno = entrada_apellido_paterno.get().upper()
    apellido_materno = entrada_apellido_materno.get().upper()
    fecha_nacimiento = entrada_fecha_nacimiento.get()
    genero = entrada_genero.get()
    entidad = entrada_entidad.get()

    # Validación de datos
    if not re.match(r"\d{2}/\d{2}/\d{4}", fecha_nacimiento):
        messagebox.showerror("Error", "La fecha de nacimiento debe estar en formato DD/MM/AAAA")
        return

    # Extraer partes para formar CURP
    try:
        dia, mes, año = fecha_nacimiento.split('/')
        curp = (apellido_paterno[0] + primer_vocal_interna(apellido_paterno) + 
                apellido_materno[0] + nombre[0] + 
                año[-2:] + mes + dia + genero + entidad +
                primera_consonante(apellido_paterno) + 
                primera_consonante(apellido_materno) + 
                primera_consonante(nombre) + "00")

        label_resultado.config(text=f"CURP generado: {curp}")
    except IndexError:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos")

# Función para obtener la primera vocal interna del apellido
def primer_vocal_interna(cadena):
    for char in cadena[1:]:
        if char in "AEIOU":
            return char
    return 'X'

# Función para obtener la primera consonante interna del apellido
def primera_consonante(cadena):
    for char in cadena[1:]:
        if char in "BCDFGHJKLMNÑPQRSTVWXYZ":
            return char
    return 'X'

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de CURP")

# Etiquetas y entradas para los datos
label_nombre = tk.Label(ventana, text="Nombre:", font=('Arial', 14))
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, font=('Arial', 14))
entrada_nombre.pack(pady=5)

label_apellido_paterno = tk.Label(ventana, text="Apellido Paterno:", font=('Arial', 14))
label_apellido_paterno.pack(pady=5)
entrada_apellido_paterno = tk.Entry(ventana, font=('Arial', 14))
entrada_apellido_paterno.pack(pady=5)

label_apellido_materno = tk.Label(ventana, text="Apellido Materno:", font=('Arial', 14))
label_apellido_materno.pack(pady=5)
entrada_apellido_materno = tk.Entry(ventana, font=('Arial', 14))
entrada_apellido_materno.pack(pady=5)

label_fecha_nacimiento = tk.Label(ventana, text="Fecha de Nacimiento (DD/MM/AAAA):", font=('Arial', 14))
label_fecha_nacimiento.pack(pady=5)
entrada_fecha_nacimiento = tk.Entry(ventana, font=('Arial', 14))
entrada_fecha_nacimiento.pack(pady=5)

label_genero = tk.Label(ventana, text="Género (H/M):", font=('Arial', 14))
label_genero.pack(pady=5)
entrada_genero = tk.Entry(ventana, font=('Arial', 14))
entrada_genero.pack(pady=5)

label_entidad = tk.Label(ventana, text="Entidad Federativa (Ej. DF, NL):", font=('Arial', 14))
label_entidad.pack(pady=5)
entrada_entidad = tk.Entry(ventana, font=('Arial', 14))
entrada_entidad.pack(pady=5)

# Botón para generar el CURP
boton_generar = tk.Button(ventana, text="Generar CURP", font=('Arial', 14), command=generar_curp)
boton_generar.pack(pady=10)

# Etiqueta para mostrar el CURP generado
label_resultado = tk.Label(ventana, text="", font=('Arial', 14))
label_resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
