# Modificación del segundo archivo
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def gestion_clientes(parent):
    """
    Crea el frame de gestión de clientes dentro de un contenedor dado (parent).
    """
    # Crear el frame principal
    frame = ttk.Frame(parent)

    # Crear la base de datos y la tabla si no existen
    sqlite3.connect("database.db")

    # Funciones CRUD (mismas que antes)
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

    def cargar_datos():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, telefono, direccion, fecha_nacimiento FROM clientes")
        filas = cursor.fetchall()
        for fila in filas:
            tree.insert("", "end", values=fila)
        conn.close()

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

    def limpiar_campos():
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_fecha_nacimiento.delete(0, tk.END)
        for item in tree.selection():
            tree.selection_remove(item)

    # Crear el formulario
    form_frame = tk.Frame(frame)
    form_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

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

    tk.Button(form_frame, text="Agregar/Actualizar", command=agregar_o_actualizar).grid(row=4, column=0)
    tk.Button(form_frame, text="Eliminar", command=eliminar_datos).grid(row=4, column=1)
    tk.Button(form_frame, text="Limpiar", command=limpiar_campos).grid(row=4, column=2)

    # Crear la tabla
    tabla_frame = tk.Frame(frame)
    tabla_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

    columns = ("ID", "Nombre", "Teléfono", "Dirección", "Fecha de Nacimiento")
    tree = ttk.Treeview(tabla_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(tabla_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.bind("<ButtonRelease-1>", seleccionar_fila)
    cargar_datos()

    return frame
