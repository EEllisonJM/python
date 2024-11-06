import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tabla Básica con Treeview")

# Definir algunos datos para la tabla (como ejemplo)
datos = [
    ("Juan", "25", "México"),
    ("Ana", "30", "España"),
    ("Luis", "22", "Argentina")
]

# Crear un Treeview para mostrar los datos en formato de tabla
columnas = ("Nombre", "Edad", "País")
tree = ttk.Treeview(ventana, columns=columnas, show="headings")

# Configurar encabezados
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.heading("País", text="País")

# Configurar tamaño de columnas
for col in columnas:
    tree.column(col, anchor="center", width=150)

# Insertar los datos en el Treeview
for fila in datos:
    tree.insert("", "end", values=fila)

# Posicionar el Treeview en la ventana
tree.pack(fill=tk.BOTH, expand=True)

# Ejecutar la ventana
ventana.mainloop()