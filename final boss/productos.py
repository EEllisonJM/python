# Modificación del segundo archivo
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def gestion_productos(parent):
    """
    Crea el frame de gestión de productos dentro de un contenedor dado (parent).
    """
    # Crear el frame principal
    frame = ttk.Frame(parent)

    # Crear la base de datos y la tabla si no existen
    sqlite3.connect("database.db")

    # Funciones CRUD (mismas que antes)
    def agregar_o_actualizar():
        nombre = entry_nombre.get().strip()
        precio = entry_precio.get().strip()
        existencia = entry_existencia.get().strip()
        caducidad = entry_caducidad.get().strip()

        if not nombre or not precio or not existencia:
            messagebox.showerror("Error", "Por favor, completa todos los campos obligatorios.")
            return

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        if tree.selection():
            # Actualizar la fila seleccionada
            item_id = tree.selection()[0]
            valores = tree.item(item_id, 'values')
            cursor.execute("""
                UPDATE productos 
                SET nombre = ?, precio = ?, existencia = ?, caducidad = ? 
                WHERE id = ?
            """, (nombre, precio, existencia, caducidad, valores[0]))
            conn.commit()
            tree.item(item_id, values=(valores[0], nombre, precio, existencia, caducidad))
        else:
            # Insertar nuevos datos
            cursor.execute("""
                INSERT INTO productos (nombre, precio, existencia, caducidad) 
                VALUES (?, ?, ?, ?)
            """, (nombre, precio, existencia, caducidad))
            conn.commit()
            tree.insert("", "end", values=(cursor.lastrowid, nombre, precio, existencia, caducidad))

        conn.close()
        limpiar_campos()

    def cargar_datos():
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio, existencia, caducidad FROM productos")
        filas = cursor.fetchall()
        for fila in filas:
            tree.insert("", "end", values=fila)
        conn.close()
        
    def obtener_producto_base_datos(id_producto):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, nombre, precio, existencia, caducidad FROM productos WHERE id={id_producto}")
        producto = cursor.fetchone()        
        conn.close()   
        return producto

    def eliminar_datos():
        if not tree.selection():
            messagebox.showwarning("Advertencia", "Por favor, selecciona un registro para eliminar.")
            return

        item_id = tree.selection()[0]
        valores = tree.item(item_id, 'values')
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (valores[0],))
        conn.commit()
        conn.close()

        tree.delete(item_id)
        limpiar_campos()

    def seleccionar_fila(event):
        for item in tree.selection():
            item_id = tree.item(item, "values")
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(tk.END, item_id[1])
            entry_precio.delete(0, tk.END)
            entry_precio.insert(tk.END, item_id[2])
            entry_existencia.delete(0, tk.END)
            entry_existencia.insert(tk.END, item_id[3])
            entry_caducidad.delete(0, tk.END)
            entry_caducidad.insert(tk.END, item_id[4])

    def limpiar_campos():
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_existencia.delete(0, tk.END)
        entry_caducidad.delete(0, tk.END)
        for item in tree.selection():
            tree.selection_remove(item)

    # Crear el formulario
    form_frame = tk.Frame(frame)
    form_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

    tk.Label(form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
    entry_nombre = tk.Entry(form_frame)
    entry_nombre.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Precio").grid(row=1, column=0, padx=5, pady=5)
    entry_precio = tk.Entry(form_frame)
    entry_precio.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Existencia").grid(row=2, column=0, padx=5, pady=5)
    entry_existencia = tk.Entry(form_frame)
    entry_existencia.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Caducidad").grid(row=3, column=0, padx=5, pady=5)
    entry_caducidad = tk.Entry(form_frame)
    entry_caducidad.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(form_frame, text="Agregar/Actualizar", command=agregar_o_actualizar).grid(row=4, column=0)
    tk.Button(form_frame, text="Eliminar", command=eliminar_datos).grid(row=4, column=1)
    tk.Button(form_frame, text="Limpiar", command=limpiar_campos).grid(row=4, column=2)

    # Crear la tabla
    tabla_frame = tk.Frame(frame)
    tabla_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

    columns = ("ID", "Nombre", "Precio", "Existencia", "Caducidad")
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
