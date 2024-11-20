import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación con Pestañas y Gráfica")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Pestaña 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Pestaña 1")
tk.Label(tab1, text="Contenido de la Pestaña 1", font=("Arial", 14)).pack(pady=20)

# Pestaña 2 - Gestión de Clientes
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Gestión de Clientes")
tk.Label(tab2, text="Aquí iría la gestión de clientes", font=("Arial", 14)).pack(pady=20)

# Pestaña 3 - Gráfica
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Gráfica de Ventas")

# Datos de ventas simuladas
ventas = [
    {"id_producto": 1, "nombre": "Papas", "cantidad": 5, "total": 50.0},
    {"id_producto": 2, "nombre": "Soda", "cantidad": 3, "total": 45.0},
    {"id_producto": 3, "nombre": "Hamburguesa", "cantidad": 7, "total": 56.0}
]

# Extraer datos para la gráfica
nombres_productos = [venta["nombre"] for venta in ventas]
totales_ventas = [venta["total"] for venta in ventas]

# Crear la gráfica
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(nombres_productos, totales_ventas, color='blue')
ax.set_title('Ventas por Producto')
ax.set_xlabel('Producto')
ax.set_ylabel('Total de Ventas')

# Integrar la gráfica en Tkinter
canvas = FigureCanvasTkAgg(fig, master=tab3)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Ejecutar la aplicación
root.mainloop()
