import sqlite3
from tkinter import ttk, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def obtener_datos_ventas():
    conexion = sqlite3.connect("database.db")  # Cambia el nombre de tu base de datos
    cursor = conexion.cursor()

    # Consulta para obtener los totales de ventas por producto
    query = """
    SELECT p.nombre, dv.subtotal
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

def actualizar_grafico(fig, ax, canvas):
    # Obtener nuevos datos
    nombres_productos, totales_ventas = obtener_datos_ventas()

    # Limpiar el gráfico actual
    ax.clear()

    # Redibujar el gráfico con nuevos datos
    ax.bar(nombres_productos, totales_ventas, color='blue')
    ax.set_title('Ventas por Producto')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Total de Ventas')
    ax.tick_params(axis='x', rotation=45)

    # Refrescar el lienzo
    canvas.draw()

def gestion_reportes(parent):
    # Crear un marco para los reportes
    ventana = ttk.Frame(parent)

    # Obtener datos iniciales desde la base de datos
    nombres_productos, totales_ventas = obtener_datos_ventas()

    # Crear el gráfico inicial
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(nombres_productos, totales_ventas, color='blue')
    ax.set_title('Ventas por Producto')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Total de Ventas')
    ax.tick_params(axis='x', rotation=45)

    # Integrar el gráfico en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill="both", expand=True)

    # Crear botón para actualizar
    boton_actualizar = Button(
        ventana,
        text="Actualizar",
        command=lambda: actualizar_grafico(fig, ax, canvas)
    )
    boton_actualizar.pack(pady=10)  # Agregar margen vertical al botón

    return ventana
