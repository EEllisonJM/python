# Ejemplo
import tkinter as tk

def registrar_venta():
    producto = entry_producto.get()
    cantidad = int(entry_cantidad.get())
    precio = float(entry_precio.get())
    total = cantidad * precio
    # Aquí va la lógica para registrar la venta y actualizar el inventario.
    label_resultado.config(text=f"Venta registrada: {producto}, Total: {total}")

root = tk.Tk()
root.title("Sistema de Ventas")

label_producto = tk.Label(root, text="Producto:")
label_producto.pack()
entry_producto = tk.Entry(root)
entry_producto.pack()

label_cantidad = tk.Label(root, text="Cantidad:")
label_cantidad.pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

label_precio = tk.Label(root, text="Precio:")
label_precio.pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

button_registrar = tk.Button(root, text="Registrar Venta", command=registrar_venta)
button_registrar.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()

