import tkinter as tk
from tkinter import ttk
from productos import gestion_productos
from clientes import gestion_clientes
from reportes import gestion_reportes  # Import the reports module
from ventas import gestion_ventas  # Import the reports module

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Información transaccional")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Cargar imágenes de iconos
icon_clientes = tk.PhotoImage(file="clientes_icon.png")
icon_productos = tk.PhotoImage(file="productos_icon.png")
icon_grafica = tk.PhotoImage(file="grafica_icon.png")

# Pestaña Ventas
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Ventas", image=icon_grafica, compound="left")
gestion_ventas(tab1).pack(fill="both", expand=True)

# Pestaña 1
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Clientes", image=icon_clientes, compound="left")
gestion_clientes(tab2).pack(fill="both", expand=True)

# Pestaña 2
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Productos", image=icon_productos, compound="left")
gestion_productos(tab3).pack(fill="both", expand=True)

# Pestaña 3
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Reportes", image=icon_grafica, compound="left")
gestion_reportes(tab4).pack(fill="both", expand=True)

#...

# Ejecutar la aplicación
root.mainloop()
