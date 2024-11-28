import sqlite3
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def obtener_datos_ventas():
    conexion = sqlite3.connect("database.db")  # Cambia el nombre de tu base de datos
    cursor = conexion.cursor()

    # Consulta para obtener los totales de ventas por producto
    query = """
    SELECT p.nombre, subtotal
    FROM detalle_de_venta dv
    JOIN productos p ON dv.id_producto = p.id
    GROUP BY p.nombre
    ORDER BY subtotal DESC;
    """
    cursor.execute(query)
    datos = cursor.fetchall()
    conexion.close()

    # Retornar los datos en forma de listas
    nombres_productos = [fila[0] for fila in datos]
    totales_ventas = [fila[1] for fila in datos]
    return nombres_productos, totales_ventas

def gestion_reportes(parent):
    # Crear un marco para los reportes
    frame = ttk.Frame(parent)

    # Obtener datos desde la base de datos
    nombres_productos, totales_ventas = obtener_datos_ventas()

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(nombres_productos, totales_ventas, color='blue')
    ax.set_title('Ventas por Producto')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Total de Ventas')
    ax.tick_params(axis='x', rotation=45)  # Rotar etiquetas en el eje X para mejor legibilidad

    # Integrar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    return frame
