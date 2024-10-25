# Ejemplo de sistema de ventas con Tkinter usando id para productos
import tkinter as tk

# Inventario con id para cada producto
inventario = {
    1: {"nombre": "Café", "cantidad": 50, "precio": 1.50},
    2: {"nombre": "Té", "cantidad": 30, "precio": 1.00},
    3: {"nombre": "Galletas", "cantidad": 100, "precio": 0.75}
}

# Función para registrar la venta
def registrar_venta():
    try:
        producto_id = int(entry_producto_id.get())
        cantidad = int(entry_cantidad.get())
    except ValueError:
        label_resultado.config(text="Error: ID o cantidad inválido.")
        return

    if producto_id in inventario and inventario[producto_id]["cantidad"] >= cantidad:
        inventario[producto_id]["cantidad"] -= cantidad
        total = cantidad * inventario[producto_id]["precio"]
        ventas.append((inventario[producto_id]["nombre"], cantidad, total))
        label_resultado.config(text=f"Venta registrada: {inventario[producto_id]['nombre']}, Total: {total:.2f}")
    else:
        label_resultado.config(text="Producto no disponible o cantidad insuficiente.")

# Función para generar reporte de ventas
def generar_reporte():
    if ventas:
        reporte = "\n".join([f"{p}, Cantidad: {c}, Total: {t:.2f}" for p, c, t in ventas])
        label_reporte.config(text=reporte)
    else:
        label_reporte.config(text="No hay ventas registradas.")

# Ventana principal de Tkinter
root = tk.Tk()
root.title("Sistema de Ventas")
root.geometry("400x300")

# Entradas y botones para la interfaz
label_producto_id = tk.Label(root, text="ID del Producto:")
label_producto_id.pack()
entry_producto_id = tk.Entry(root)
entry_producto_id.pack()

label_cantidad = tk.Label(root, text="Cantidad:")
label_cantidad.pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

button_venta = tk.Button(root, text="Registrar Venta", command=registrar_venta)
button_venta.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

button_reporte = tk.Button(root, text="Generar Reporte", command=generar_reporte)
button_reporte.pack()

label_reporte = tk.Label(root, text="")
label_reporte.pack()

# Lista para registrar ventas
ventas = []

# Ejecutar la ventana principal
root.mainloop()
