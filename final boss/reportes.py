from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def gestion_reportes(parent):
    """
    Creates and packs the report interface into the provided parent widget.
    """
    # Create a frame for the reports
    frame = ttk.Frame(parent)

    # Example sales data
    ventas = [
        {"id_producto": 1, "nombre": "Papas", "cantidad": 5, "total": 50.0},
        {"id_producto": 2, "nombre": "Soda", "cantidad": 3, "total": 45.0},
        {"id_producto": 3, "nombre": "Hamburguesa", "cantidad": 7, "total": 56.0}
    ]

    # Extract data for the graph
    nombres_productos = [venta["nombre"] for venta in ventas]
    totales_ventas = [venta["total"] for venta in ventas]

    # Create the graph
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(nombres_productos, totales_ventas, color='blue')
    ax.set_title('Ventas por Producto')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Total de Ventas')

    # Integrate the graph into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    return frame
