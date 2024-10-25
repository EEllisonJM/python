import tkinter as tk
from tkinter import ttk, messagebox

# Inventario con id para cada producto
productos = {
    1: {"nombre": "Papas fritas", "precio": 10.0},
    2: {"nombre": "Soda", "precio": 15.0},
    3: {"nombre": "Hamburguesa", "precio": 8.0}
}

# Lista para registrar ventas
ventas = []

# Función para agregar el producto al detalle de la venta
def agregar_producto():
    try:
        id_producto = int(entry_id_producto.get())
        cantidad = int(entry_cantidad.get())

        if id_producto in productos:
            producto = productos[id_producto]
            nombre = producto["nombre"]
            precio = producto["precio"]
            importe = precio * cantidad

            # Agregar los datos a la tabla
            tree.insert("", "end", values=(id_producto, nombre, f"${precio:.2f}", cantidad, f"${importe:.2f}"))
            ventas.append((id_producto, cantidad, importe))  # Registrar venta
            calcular_total()

            # Limpiar las entradas
            entry_id_producto.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Producto no encontrado")
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Asegúrate de ingresar números enteros.")

# Función para calcular el total de la venta
def calcular_total():
    total = 0.0
    for item in tree.get_children():
        importe_str = tree.item(item, "values")[4]
        importe = float(importe_str.replace("$", ""))
        total += importe
    label_total.config(text=f"Total: ${total:.2f}")

# Función para procesar la venta
def procesar_venta():
    total_str = label_total.cget("text").replace("Total: $", "")
    try:
        total = float(total_str)
        pago = float(entry_pago.get())
        if total > 0 and pago > 0:
            if pago < total:
                messagebox.showerror("Error", "El pago es insuficiente.")
            else:
                cambio = pago - total
                messagebox.showinfo("Venta Procesada", f"Venta procesada exitosamente.\nCambio: ${cambio:.2f}")
                reset_venta()
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida en el pago. Asegúrate de ingresar un número válido.")

# Función para reiniciar la venta después de procesarla
def reset_venta():
    # Limpiar la tabla
    for item in tree.get_children():
        tree.delete(item)
    # Resetear el total
    label_total.config(text="Total: $0.00")
    # Limpiar el pago
    entry_pago.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema POS Simple")

# Configurar el grid para mejor disposición
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

# Crear los widgets de entrada
label_id_producto = tk.Label(root, text="ID Producto:")
label_id_producto.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_id_producto = tk.Entry(root)
entry_id_producto.grid(row=0, column=1, padx=5, pady=5, sticky="w")

label_cantidad = tk.Label(root, text="Cantidad:")
label_cantidad.grid(row=0, column=2, padx=5, pady=5, sticky="e")
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=0, column=3, padx=5, pady=5, sticky="w")

button_agregar = tk.Button(root, text="Agregar", command=agregar_producto)
button_agregar.grid(row=0, column=4, padx=5, pady=5)

# Crear la tabla para mostrar el detalle de la venta
columns = ("ID Producto", "Nombre", "Precio", "Cantidad", "Importe")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

tree.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Agregar una scrollbar a la tabla
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=5, sticky='ns')

# Etiqueta para mostrar el total
label_total = tk.Label(root, text="Total: $0.00", font=("Arial", 14, "bold"))
label_total.grid(row=2, column=0, columnspan=5, padx=5, pady=10, sticky="w")

# Entrada y etiqueta para el pago
label_pago = tk.Label(root, text="Pago:")
label_pago.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_pago = tk.Entry(root)
entry_pago.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Botón para procesar la venta
button_procesar = tk.Button(root, text="Procesar Venta", command=procesar_venta, bg="green", fg="white")
button_procesar.grid(row=4, column=0, columnspan=5, padx=5, pady=10)

# Configurar el grid para que la tabla se expanda correctamente
root.rowconfigure(1, weight=1)
root.columnconfigure(4, weight=1)

# Iniciar el loop principal de la ventana
root.mainloop()
