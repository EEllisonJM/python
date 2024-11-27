import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# Eliminar la base de datos (solo para pruebas, peligroso en producción)
def eliminar_db():
    archivo = "database.db"
    try:
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo '{archivo}' eliminado exitosamente.")
        else:
            print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

# 1 Conectar o crear la base de datos
def conectar_db():
    sqlite3.connect("database.db")

# Agregar o actualizar los datos
def agregar_o_actualizar():
    nombre = entry_nombre.get().strip()
    telefono = entry_telefono.get().strip()
    direccion = entry_direccion.get().strip()
    fecha_nacimiento = entry_fecha_nacimiento.get().strip()

    if not nombre or not telefono or not direccion:
        messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if tree.selection():
        # Actualizar la fila seleccionada
        item_id = tree.selection()[0]
        valores = tree.item(item_id, 'values')
        cursor.execute("""
            UPDATE clientes 
            SET nombre = ?, telefono = ?, direccion = ?, fecha_nacimiento = ? 
            WHERE id = ?
        """, (nombre, telefono, direccion, fecha_nacimiento, valores[0]))
        conn.commit()
        tree.item(item_id, values=(valores[0], nombre, telefono, direccion, fecha_nacimiento))
    else:
        # Insertar nuevos datos
        cursor.execute("""
            INSERT INTO clientes (nombre, telefono, direccion, fecha_nacimiento) 
            VALUES (?, ?, ?, ?)
        """, (nombre, telefono, direccion, fecha_nacimiento))
        conn.commit()
        tree.insert("", "end", values=(cursor.lastrowid, nombre, telefono, direccion, fecha_nacimiento))

    conn.close()
    limpiar_campos()

# Cargar los datos de la base de datos
def cargar_datos():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, telefono, direccion, fecha_nacimiento FROM clientes")
    filas = cursor.fetchall()
    for fila in filas:
        tree.insert("", "end", values=fila)
    conn.close()

# Eliminar los datos seleccionados
def eliminar_datos():
    if not tree.selection():
        messagebox.showwarning("Advertencia", "Por favor, selecciona un registro para eliminar.")
        return

    item_id = tree.selection()[0]
    valores = tree.item(item_id, 'values')
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (valores[0],))
    conn.commit()
    conn.close()

    tree.delete(item_id)
    limpiar_campos()

# Seleccionar una fila para mostrar sus datos
def seleccionar_fila(event):
    for item in tree.selection():
        item_id = tree.item(item, "values")
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(tk.END, item_id[1])
        entry_telefono.delete(0, tk.END)
        entry_telefono.insert(tk.END, item_id[2])
        entry_direccion.delete(0, tk.END)
        entry_direccion.insert(tk.END, item_id[3])
        entry_fecha_nacimiento.delete(0, tk.END)
        entry_fecha_nacimiento.insert(tk.END, item_id[4])

# Limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_fecha_nacimiento.delete(0, tk.END)
    for item in tree.selection():
        tree.selection_remove(item)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Clientes")

ventana.geometry("800x500")

# Crear la base de datos y la tabla si no existen
conectar_db()

# Crear el formulario para agregar datos
form_frame = tk.Frame(ventana)
form_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

# Etiquetas y campos de texto en el formulario
tk.Label(form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(form_frame)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Teléfono").grid(row=1, column=0, padx=5, pady=5)
entry_telefono = tk.Entry(form_frame)
entry_telefono.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Dirección").grid(row=2, column=0, padx=5, pady=5)
entry_direccion = tk.Entry(form_frame)
entry_direccion.grid(row=2, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Fecha de Nacimiento").grid(row=3, column=0, padx=5, pady=5)
entry_fecha_nacimiento = tk.Entry(form_frame)
entry_fecha_nacimiento.grid(row=3, column=1, padx=5, pady=5)

# Botones para las operaciones CRUD
boton_agregar_actualizar = tk.Button(form_frame, text="Agregar/Actualizar", command=agregar_o_actualizar)
boton_agregar_actualizar.grid(row=4, column=0)

boton_eliminar = tk.Button(form_frame, text="Eliminar", command=eliminar_datos)
boton_eliminar.grid(row=4, column=1)

boton_limpiar = tk.Button(form_frame, text="Limpiar", command=limpiar_campos)
boton_limpiar.grid(row=4, column=2)

# Crear un frame para la tabla
tabla_frame = tk.Frame(ventana)
tabla_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear la tabla con Treeview
columns = ("ID", "Nombre", "Teléfono", "Dirección", "Fecha de Nacimiento")
tree = ttk.Treeview(tabla_frame, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Teléfono", text="Teléfono")
tree.heading("Dirección", text="Dirección")
tree.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")

for col in columns:
    tree.column(col, anchor="center", width=150)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Agregar scrollbar
scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Evento para seleccionar una fila
tree.bind("<ButtonRelease-1>", seleccionar_fila)

# Cargar los datos al iniciar la aplicación
cargar_datos()

# Ejecutar la ventana
ventana.mainloop()
